# coding=utf-8
# Copyright 2017 Flowdas Inc. <prospero@flowdas.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from __future__ import absolute_import

import collections
import functools
import multiprocessing
import os
import signal
import time

import click
import falcon
import gevent
import gunicorn.app.base
import gunicorn.util

from flowdas import meta
from .app import App
from .base import define, command, Path, _profile, _timeit
from .testing import simulate_request

try:
    from setproctitle import setproctitle


    def _setproctitle(title):
        setproctitle("Oliver: %s" % title)


    gunicorn.util._setproctitle = _setproctitle
except:
    pass

__all__ = [
]

# define setting parameters
define('SERVER_ADDR', meta.String(default='127.0.0.1'))
define('SERVER_PORT', meta.Integer(default=8000))
define('BACKLOG', meta.Integer(default=2048))
define('WORKER_CONNECTIONS', meta.Integer(default=10000))
define('PIDFILE', Path(default='Oliver.pid'))
define('OMX', meta.String())
define('OMX_ALLOW', meta.String(default='*'))
define('OMX_PROFILE_INTERVAL', meta.Float(default=0.001))
define('OMX_PROFILE_THRESHOLD', meta.Integer(default=0))


class Application(gunicorn.app.base.BaseApplication):
    routes = {}
    sinks = {}

    def __init__(self, daemon=False):
        self.application = App.wsgi
        from flowdas import oliver

        if oliver.config.OMX:
            self.profiler = OMXProfiler()
            self.profiler.start()
            App().add_route(oliver.config.OMX + '/stack', self.profiler)

        debug = oliver.config.DEBUG
        if daemon:
            gunicorn.util.daemonize(False)
        self.options = {
            'bind': '%s:%s' % ('127.0.0.1' if debug else oliver.config.SERVER_ADDR, oliver.config.SERVER_PORT),
            'workers': multiprocessing.cpu_count() * 2 if daemon else 1,
            'backlog': oliver.config.BACKLOG,
            'worker_connections': oliver.config.WORKER_CONNECTIONS,
            'errorlog': oliver.config.LOGFILE if daemon else '-',
            'loglevel': oliver.config.LOGLEVEL,
            'capture_output': True,
        }
        if oliver.config.PIDFILE:
            self.options['pidfile'] = oliver.config.PIDFILE
        super(Application, self).__init__()
        self.cfg.set('worker_class', 'flowdas.oliver.gunicorn')
        self.cfg.set('proc_name', oliver.config.OLIVERFILE)

    def load_config(self):
        config = dict([(key, value) for key, value in self.options.items()
                       if key in self.cfg.settings and value is not None])
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self):
        from flowdas import oliver
        if oliver.config.OMX and oliver.config.OMX_PROFILE_THRESHOLD > 0:
            def app(*args):
                # OMXProfiler 가 사용한다.
                __omx_epoch__ = time.time()
                return self.application(*args)

            return app
        else:
            return self.application


#
# OMX
#

class OMXProfiler(object):
    def __init__(self):
        self.stack_counts = collections.defaultdict(int)
        self.started = None

    def __del__(self):
        self.stop()

    def _sample(self, signum, frame):
        from flowdas import oliver
        stack = []
        epoch = None
        while frame is not None:
            formatted_frame = '{}({})'.format(frame.f_code.co_name, frame.f_globals.get('__name__'))
            if epoch is None:
                epoch = frame.f_locals.get('__omx_epoch__')
            stack.append(formatted_frame)
            frame = frame.f_back

        if oliver.config.OMX_PROFILE_THRESHOLD <= 0 or (
                        epoch is not None and oliver.config.OMX_PROFILE_THRESHOLD <= time.time() - epoch):
            formatted_stack = ';'.join(reversed(stack))
            self.stack_counts[formatted_stack] += 1
        signal.setitimer(signal.ITIMER_VIRTUAL, oliver.config.OMX_PROFILE_INTERVAL, 0)

    def reset(self):
        self.started = time.time()
        self.stack_counts = collections.defaultdict(int)

    def start(self):
        from flowdas import oliver
        self.started = time.time()
        signal.signal(signal.SIGVTALRM, self._sample)
        signal.setitimer(signal.ITIMER_VIRTUAL, oliver.config.OMX_PROFILE_INTERVAL, 0)

    def stop(self):
        if self.started is not None:
            self.reset()
            signal.setitimer(signal.ITIMER_VIRTUAL, 0)
            self.started = None

    def on_get(self, req, resp):
        from flowdas import oliver
        if oliver.config.OMX_ALLOW != '*':
            if not isinstance(oliver.config.OMX_ALLOW, (list, tuple, set)):
                allow = [oliver.config.OMX_ALLOW]
            else:
                allow = oliver.config.OMX_ALLOW
            if req.access_route[0] not in allow:
                raise falcon.HTTPNotFound()
        resp.content_type = 'text/plain'
        if self.started:
            ordered_stacks = sorted(self.stack_counts.items(), key=lambda kv: kv[1], reverse=True)
            resp.body = '\n'.join('{} {}'.format(frame, count) for frame, count in ordered_stacks) + '\n'

        if req.get_param('reset') == 'true':
            self.reset()


@command(help='Run server in development mode.')
def develop():
    Application().run()


@command(help='Run server in production mode.')
def serve():
    Application(daemon=True).run()


def signal_server(sig, echo=False, wait=False):
    from flowdas import oliver
    if oliver.config.PIDFILE and os.path.exists(oliver.config.PIDFILE):
        with open(oliver.config.PIDFILE) as f:
            pid = int(f.read().strip())
            if echo:
                click.echo(pid)
        os.kill(pid, sig)
        while wait:
            try:
                os.kill(pid, 0)
                gevent.sleep(1)
            except:
                break


@command(help='Shutdown running servers.')
@click.option('--quick', '-C', is_flag=True, help='Quick shutdown.')
def shutdown(quick):
    signal_server(signal.SIGINT if quick else signal.SIGTERM, echo=True, wait=True)


@command(help='Reopen the log files.')
def logrotate():
    signal_server(signal.SIGUSR1)


def http_request(*args, **kwargs):
    r = simulate_request(*args, **kwargs)
    click.echo('HTTP/1.1 %s' % r.status)
    for name in r.headers:
        click.echo('%s: %s' % (name, r.headers[name]))
    click.echo('')
    if r.content:
        click.echo(r.content)


@command(help='Simulate Http request.')
@click.option('-t', '--timeit', is_flag=True, help='Measure request time.')
@click.option('-p', '--profile', is_flag=True, help='Enable profiling.')
@click.option('-o', '--output', default='Oliver.prof', help='Profile output file.')
@click.option('-n', '--number', default=1, help='Execute the given command INTEGER times in a loop.')
@click.option('-r', '--repeat', default=3, help='Repeat the loop iteration INTEGER times and take the best result. [3]')
@click.argument('method')
@click.argument('path')
@click.argument('args', nargs=-1)
def http(timeit, profile, output, number, repeat, method, path, args):
    headers = {}
    params = {}
    body = []

    def add_param(key, value):
        if key == 'body':
            body.append(value or '')
        else:
            if key in params:
                params[key].append(val)
            else:
                params[key] = [val]

    for arg in args:
        n = len(arg)
        idx = min(arg.find(':') % (n + 1), arg.find('=') % (n + 1))
        if idx == n:
            key = arg.strip()
            add_param(key, None)
        else:
            sep = arg[idx]
            key = arg[:idx].strip()
            val = arg[idx + 1:].strip()
            if sep == '=':
                add_param(key, val)
            else:
                headers[key] = val
    opts = {}
    if params:
        opts['params'] = params
    if headers:
        opts['headers'] = headers
    if body:
        opts['body'] = ''.join(body)

    if profile:
        from falcon.testing import TestClient
        client = TestClient(App.wsgi)

        fut = functools.partial(client.simulate_request, method, path, **opts)
        _profile(fut, output=output, number=number)
    elif timeit:
        from falcon.testing import TestClient
        client = TestClient(App.wsgi)

        fut = functools.partial(client.simulate_request, method, path, **opts)
        _timeit(fut, number=number, repeat=repeat)
    else:
        r = simulate_request(method, path, **opts)
        click.echo('HTTP/1.1 %s' % r.status)
        for name in r.headers:
            click.echo('%s: %s' % (name, r.headers[name]))
        click.echo('')
        if r.content:
            click.echo(r.content)


@command(help='Simulate Http GET.')
@click.option('-t', '--timeit', is_flag=True, help='Measure request time.')
@click.option('-p', '--profile', is_flag=True, help='Enable profiling.')
@click.option('-o', '--output', default='Oliver.prof', help='Profile output file.')
@click.option('-n', '--number', default=1, help='Execute the given command INTEGER times in a loop.')
@click.option('-r', '--repeat', default=3, help='Repeat the loop iteration INTEGER times and take the best result. [3]')
@click.argument('path')
@click.argument('args', nargs=-1)
@click.pass_context
def get(ctx, **kwargs):
    ctx.invoke(http, method='GET', **kwargs)


@command(help='Simulate Http POST.')
@click.option('-t', '--timeit', is_flag=True, help='Measure request time.')
@click.option('-p', '--profile', is_flag=True, help='Enable profiling.')
@click.option('-o', '--output', default='Oliver.prof', help='Profile output file.')
@click.option('-n', '--number', default=1, help='Execute the given command INTEGER times in a loop.')
@click.option('-r', '--repeat', default=3, help='Repeat the loop iteration INTEGER times and take the best result. [3]')
@click.argument('path')
@click.argument('args', nargs=-1)
@click.pass_context
def post(ctx, **kwargs):
    ctx.invoke(http, method='POST', **kwargs)


@command(help='Simulate Http PUT.')
@click.option('-t', '--timeit', is_flag=True, help='Measure request time.')
@click.option('-p', '--profile', is_flag=True, help='Enable profiling.')
@click.option('-o', '--output', default='Oliver.prof', help='Profile output file.')
@click.option('-n', '--number', default=1, help='Execute the given command INTEGER times in a loop.')
@click.option('-r', '--repeat', default=3, help='Repeat the loop iteration INTEGER times and take the best result. [3]')
@click.argument('path')
@click.argument('args', nargs=-1)
@click.pass_context
def put(ctx, **kwargs):
    ctx.invoke(http, method='PUT', **kwargs)


@command(help='Simulate Http PATCH.')
@click.option('-t', '--timeit', is_flag=True, help='Measure request time.')
@click.option('-p', '--profile', is_flag=True, help='Enable profiling.')
@click.option('-o', '--output', default='Oliver.prof', help='Profile output file.')
@click.option('-n', '--number', default=1, help='Execute the given command INTEGER times in a loop.')
@click.option('-r', '--repeat', default=3, help='Repeat the loop iteration INTEGER times and take the best result. [3]')
@click.argument('path')
@click.argument('args', nargs=-1)
@click.pass_context
def patch(ctx, **kwargs):
    ctx.invoke(http, method='PATCH', **kwargs)


@command(help='Simulate Http DELETE.')
@click.option('-t', '--timeit', is_flag=True, help='Measure request time.')
@click.option('-p', '--profile', is_flag=True, help='Enable profiling.')
@click.option('-o', '--output', default='Oliver.prof', help='Profile output file.')
@click.option('-n', '--number', default=1, help='Execute the given command INTEGER times in a loop.')
@click.option('-r', '--repeat', default=3, help='Repeat the loop iteration INTEGER times and take the best result. [3]')
@click.argument('path')
@click.argument('args', nargs=-1)
@click.pass_context
def delete(ctx, **kwargs):
    ctx.invoke(http, method='DELETE', **kwargs)
