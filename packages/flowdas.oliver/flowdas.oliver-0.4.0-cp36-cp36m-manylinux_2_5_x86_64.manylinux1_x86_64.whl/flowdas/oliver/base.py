# coding=utf-8
# Copyright 2017 Flowdas Inc. <prospero@flowdas.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from __future__ import absolute_import

import sys

PY2 = (sys.version_info[0] == 2)
PY3 = (sys.version_info[0] == 3)

import os
import logging
import signal
import importlib
import functools

import click
from pkg_resources import get_distribution

from gevent import monkey
import yaml

from flowdas import meta

__all__ = [
    '__author__',
    '__version__',
    'define',
    'ready',
    'command',
    'Path',
    'PY2',
    'PY3',
    'critical',
    'error',
    'warning',
    'info',
    'debug',
    'exception',
    'config',
]

__author__ = u'오동권(Dong-gweon Oh) <prospero@flowdas.com>'
__version__ = getattr(get_distribution('flowdas.oliver'), 'version', None)

if PY3:
    def execfile(filename, globals):
        with open(filename) as f:
            source = f.read()
        code = compile(source, filename, 'exec')
        exec(code, globals)


#
# config
#

class _Config(object):
    def __getattr__(self, item):
        raise ImportError('Oliver packages should be declared in a file named oliver.yaml.')


config = _Config()

_params = {}

OLIVER_PATH = None


def create_config():
    Config = meta.Entity.define_subclass('Config', _params)
    return Config()


class Path(meta.String):
    """
    경로명을 표현하는 :py:class:`flowdas.meta.Property`.

    상대 경로명이 제공되면 ``oliver.yaml`` 과의 상대 경로로 해석되고, 절대 경로로 변환된다.

    :py:class:`flowdas.meta.String` 의 모든 옵션을 지원한다.

    Since version 0.3.
    """

    def _load_(self, value, context):
        value = super(Path, self)._load_(value, context)
        return os.path.normpath(os.path.join(OLIVER_PATH, value))


def define(name, prop=None):
    """설정 파라미터를 정의한다.

    name 은 파라미터의 이름.

    prop 는 파라미터의 형을 지정하는 :py:class:`flowdas.meta.Property` 인스턴스. 생략하면 :py:class:`flowdas.meta.String` ().

    Since version 0.2.
    """
    if prop is None:
        prop = meta.String()
    _params[name] = prop


define('DEBUG', meta.Boolean())
define('OLIVERFILE', meta.String())
define('PYTHONPATH', Path[:]().apply_options(default=()))
define('ENV', meta.JsonObject(default={}))
define('CHDIR', Path(default='.'))
define('LOGLEVEL', meta.String(default='info'))
define('LOGFILE', Path(default='Oliver.log'))


class OliverfileNotFoundError(Exception):
    def __init__(self, oliverfile):
        super(OliverfileNotFoundError, self).__init__()
        self.oliverfile = oliverfile


_pending = set()


def setup(oliverfile, debug=False):
    global OLIVER_PATH, config
    if OLIVER_PATH is None:
        OLIVER_PATH = ''
        os.environ.setdefault('LC_CTYPE', 'ko_KR.UTF-8')
        monkey.patch_all(subprocess=True)

        if oliverfile is None:
            oliverfile = 'oliver.yaml'
        oliverfile = os.path.abspath(oliverfile)
        if not os.path.isfile(oliverfile):
            raise OliverfileNotFoundError(oliverfile)

        OLIVER_PATH = os.path.dirname(oliverfile)

        with open(oliverfile, 'rb') as f:
            context = yaml.load(f)
        if context is None:
            context = {}

        context['DEBUG'] = debug
        context['OLIVERFILE'] = oliverfile
        if debug:
            context.setdefault('LOGLEVEL', 'debug')

        if 'PYTHONPATH' in context:
            sys.path.extend(context['PYTHONPATH'])
        if 'ENV' in context:
            os.environ.update(config.ENV)

        retry_import = OLIVER_PATH not in sys.path

        if 'uses' in context:
            for modname in context['uses']:
                try:
                    module = importlib.import_module(modname)
                except ImportError:
                    if retry_import:
                        retry_import = False
                        sys.path.append(OLIVER_PATH)
                        module = importlib.import_module(modname)
                        if isinstance(context.get('PYTHONPATH'), (list, tuple)):
                            context['PYTHONPATH'] = list(context['PYTHONPATH'])
                            context['PYTHONPATH'].append(OLIVER_PATH)
                        else:
                            context['PYTHONPATH'] = (OLIVER_PATH,)
                    else:
                        raise

        Config = meta.Entity.define_subclass('Config', _params)
        config = Config().load(context)
        from flowdas import oliver
        oliver.config = config

        if config.CHDIR:
            os.chdir(config.CHDIR)

        if _pending:
            from .app import App
            for func in _pending:
                App.invoke_ready(func)
            _pending.clear()


def ready(func):
    """``oliver.yaml`` 로딩이 완료될 때 호출될 함수를 등록하는 데코레이터.

    :py:data:`config` 를 필요로 하는 초기화나 App 인스턴스 별로 라우팅을 설정하고자 할 때 사용한다.

    func
        func(app) 형태로 호출된다. app 은 :py:class:`App` 인스턴스. app 이 여러개 있으면 모든 인스턴스에 대해 한번씩 호출된다.

    이미 로딩이 완료된 상태면 즉시 호출된다.

    Since version 0.3.
    """
    if isinstance(config, _Config):
        _pending.add(func)
    else:
        from .app import App
        App.invoke_ready(func)


#
# logging
#

class Logger(object):
    LOG_LEVELS = {
        "critical": logging.CRITICAL,
        "error": logging.ERROR,
        "warning": logging.WARNING,
        "info": logging.INFO,
        "debug": logging.DEBUG
    }

    def __init__(self):
        self.log = logging.getLogger('oliver')
        self.log.propagate = False
        if config.LOGFILE and config.LOGFILE != '-':
            dirname = os.path.dirname(config.LOGFILE)
            if not os.path.exists(dirname):
                os.makedirs(dirname)
            self.handler = logging.FileHandler(config.LOGFILE)
            self.sighandler = signal.signal(signal.SIGUSR1, self.handle_usr1)
        else:
            self.handler = logging.StreamHandler(sys.stdout)
        logfmt = r"%(asctime)s [%(process)d] [%(levelname)s] %(message)s"
        datefmt = r"[%Y-%m-%d %H:%M:%S %z]"
        self.handler.setFormatter(logging.Formatter(logfmt, datefmt))
        self.log.addHandler(self.handler)
        self.log.setLevel(self.LOG_LEVELS.get(config.LOGLEVEL, logging.INFO))

    def handle_usr1(self, sig, frame):
        if self.sighandler:
            self.sighandler(sig, frame)
        self.reopen_files()

    def reopen_files(self):
        handler = self.handler
        handler.acquire()
        try:
            if handler.stream:
                handler.stream.close()
                handler.stream = open(handler.baseFilename, handler.mode)
        finally:
            handler.release()


_logger = None


def logger():
    global _logger
    if _logger is None:
        _logger = Logger()
    return _logger


def critical(msg, *args, **kwargs):
    """*CRITICAL* 수준으로 메시지를 로그한다. 인자는 :py:func:`logging.critical` 처럼 해석된다.

    Since version 0.2.
    """
    logger().log.critical(msg, *args, **kwargs)


def error(msg, *args, **kwargs):
    """*ERROR* 수준으로 메시지를 로그한다. 인자는 :py:func:`logging.error` 처럼 해석된다.

    Since version 0.2.
    """
    logger().log.error(msg, *args, **kwargs)


def warning(msg, *args, **kwargs):
    """*WARNING* 수준으로 메시지를 로그한다. 인자는 :py:func:`logging.warning` 처럼 해석된다.

    Since version 0.2.
    """
    logger().log.warning(msg, *args, **kwargs)


def info(msg, *args, **kwargs):
    """*INFO* 수준으로 메시지를 로그한다. 인자는 :py:func:`logging.info` 처럼 해석된다.

    Since version 0.2.
    """
    logger().log.info(msg, *args, **kwargs)


def debug(msg, *args, **kwargs):
    """*DEBUG* 수준으로 메시지를 로그한다. 인자는 :py:func:`logging.debug` 처럼 해석된다.

    Since version 0.2.
    """
    logger().log.debug(msg, *args, **kwargs)


def exception(msg, *args, **kwargs):
    """*ERROR* 수준으로 메시지를 로그한다. 인자는 :py:func:`logging.exception` 처럼 해석된다.

    Since version 0.2.
    """
    logger().log.exception(msg, *args, **kwargs)


#
# command line interface
#

class Cli(click.Group):
    def invoke(self, ctx):
        try:
            setup(ctx.params['file'], ctx.params['debug'])
        except OliverfileNotFoundError as e:
            click.echo("No Oliverfile found: %s\n" % e.oliverfile)
            click.echo(ctx.get_help(), color=ctx.color)
            ctx.exit()
        super(Cli, self).invoke(ctx)


@click.command(cls=Cli, invoke_without_command=True)
@click.option('-f', '--file', type=click.Path('rb'), metavar='FILE', help='Read FILE as an Oliverfile.')
@click.option('-d', '--debug', is_flag=True, help='Enable debugging outputs.')
@click.pass_context
def cli(ctx, file, debug):
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help(), color=ctx.color)
        ctx.exit()


def command(*args, **kwargs):
    """명령행 인터페이스에 명령을 추가하는 데코레이터.

    인자는 :py:func:`click.command` 의 정의를 따른다.

    Example:

        >>> from flowdas import oliver
        >>> import click
        >>>
        >>> @oliver.command(help='Echo text')
        ... @click.argument('text')
        ... def echo(text):
        ...     click.echo(text)

    Since version 0.2.
    """

    def deco(func):
        return cli.command(*args, **kwargs)(func)

    return deco


@command(help='Print version string.')
def version():
    click.echo(__version__)


@command(help='Show settings.')
def settings():
    for name in sorted(_params):
        value = getattr(config, name)
        if callable(value):
            modname = value.__module__
            if not modname:
                modname = 'OLIVERFILE'
            click.echo('%s = %s.%s' % (name, modname, value.__name__))
        else:
            click.echo('%s = %r' % (name, value))


def _timeit(fut, number, repeat):
    import timeit
    context = {'fut': fut}
    best = min(timeit.repeat('fut()', repeat=repeat, number=number, globals=context))
    usec = best * 1e6 / number
    msgs = []
    msgs.append("%d loops," % number)
    precision = 3
    units = {"usec": 1, "msec": 1e3, "sec": 1e6}
    scales = [(scale, unit) for unit, scale in units.items()]
    scales.sort(reverse=True)
    for scale, time_unit in scales:
        if usec >= scale:
            break
    msgs.append("best of %d: %.*g %s per loop" % (repeat, precision, usec / scale, time_unit))
    click.echo(' '.join(msgs))


@command(help='Time execution of a command.')
@click.option('-n', '--number', default=1, help='Execute the given command INTEGER times in a loop.')
@click.option('-r', '--repeat', default=3, help='Repeat the loop iteration INTEGER times and take the best result. [3]')
@click.argument('command')
@click.argument('args', nargs=-1)
def timeit(number, repeat, command, args):
    from .testing import simulate_command
    fut = functools.partial(simulate_command, *((command,) + args))
    _timeit(fut, number=number, repeat=repeat)


def _profile(fut, output, number):
    import cProfile
    def run():
        for i in range(number):
            fut()

    context = {'run': run}
    cProfile.runctx('run()', globals=context, locals=context, filename=output)


@command(help='Time execution of a command.')
@click.option('-o', '--output', default='Oliver.prof', help='Output file.')
@click.option('-n', '--number', default=1, help='Execute the given command INTEGER times in a loop.')
@click.argument('command')
@click.argument('args', nargs=-1)
def profile(output, number, command, args):
    from click.testing import CliRunner

    runner = CliRunner()
    fut = functools.partial(runner.invoke, cli, (command,) + args)
    _profile(fut, output=output, number=number)


def main():
    cli()
