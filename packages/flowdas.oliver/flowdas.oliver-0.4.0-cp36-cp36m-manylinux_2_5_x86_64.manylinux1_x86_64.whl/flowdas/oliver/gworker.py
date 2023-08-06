# coding=utf-8
# Copyright 2016 Flowdas Inc. <prospero@flowdas.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from __future__ import absolute_import

import socket
import time

import gevent
import gunicorn.util as util
from gevent.pywsgi import format_date_time
from gunicorn.http.wsgi import WSGIErrorsWrapper
from gunicorn.workers.ggevent import GeventWorker

from .base import __version__, PY3
from .parser import WsgiParser, HttpParserError

if PY3:
    def _S(b):
        return b.decode()


    def _B(s):
        return s.encode()


    def reraise(exc_info):
        raise exc_info[1].with_traceback(exc_info[2])

else:
    def _S(b):
        return b


    def _B(s):
        return s


    exec("""def reraise(exc_info):
    raise exc_info[0], exc_info[1], exc_info[2]
""")

_HOP_BY_HOP_HEADERS = {
    'connection',
    'keep-alive',
    'proxy-authenticate',
    'trailer',
    'transfer-encoding',
    'upgrade',
    # 'proxy-authorization',
    # 'te',
}


class Input(object):
    def read(self, size=-1):
        return b''

    def readline(self, size=-1):
        return b''

    def readlines(self, hint=-1):
        return []

    def __iter__(self):
        for data in ():
            yield data


class Stream(object):
    NULL = Input()

    def get_input(self):
        return self.NULL

    def get_output(self):
        return None


class BodyStream(Stream):
    def __init__(self):
        self._sp = socket.socketpair()
        self._if = self._sp[0].makefile('rb')

    def get_input(self):
        return self._if

    def get_output(self):
        return self._sp[1]

    def close(self):
        self._sp[1].close()
        self._if.close()
        self._sp[0].close()
        self._if = None
        self._sp = None


class Protocol(WsgiParser):
    def __init__(self, worker, client, addr, listener):
        super(Protocol, self).__init__()
        self._worker = worker
        self._client = client
        self._done = False
        server_name, server_port = self.guess_server(listener)
        self._env = {
            'REMOTE_ADDR': addr[0],
            'wsgi.version': (1, 0),
            'wsgi.multithread': True,
            'wsgi.multiprocess': True,
            'wsgi.run_once': False,
            'wsgi.input': Stream.NULL,
            'wsgi.errors': worker.wsgi_errors,
        }
        self._env.setdefault('wsgi.url_scheme', 'http')
        self._env.setdefault('SERVER_NAME', server_name)
        self._env.setdefault('SERVER_PORT', server_port)

    def guess_server(self, listener):
        if isinstance(listener, str):
            listener = listener.split(":")
        return listener[0], str(listener[1])

    def run(self):
        try:
            while not self._done:
                try:
                    data = self._client.recv(4096)
                except IOError:
                    data = None
                if not data:
                    break
                self.execute(data)
        except HttpParserError as e:
            util.write_error(self._client, 400, 'Bad Request', '%s' % e.args)

    def check_content_length(self, data):
        if self._content_length is not None and self._sent_bytes + len(data) > self._content_length:
            raise AssertionError('Cannot write more than Content-Length %d' % self._content_length)
        self._sent_bytes += len(data)

    def on_request(self, environ):
        te = environ.pop('HTTP_TRANSFER_ENCODING', None)
        if te:
            tes = map(lambda x: x.strip(), te.split(','))
            if tes:
                if tes[-1] == 'chunked':
                    tes.pop()
                    if tes:
                        environ['HTTP_TRANSFER_ENCODING'] = ','.join(tes)
        for key in ('HTTP_CONNECTION', 'HTTP_KEEP_ALIVE', 'HTTP_PROXY_AUTHENTICATE', 'HTTP_TRAILER', 'HTTP_UPGRADE',
                    'HTTP_PROXY_AUTHORIZATION', 'HTTP_TE'):
            environ.pop(key, None)
        if 'HTTP_CONTENT_TYPE' in environ:
            environ['CONTENT_TYPE'] = environ['HTTP_CONTENT_TYPE']
        if 'HTTP_CONTENT_LENGTH' in environ:
            environ['CONTENT_LENGTH'] = environ['HTTP_CONTENT_LENGTH']
        environ.update(self._env)

        self._method = None
        self._chunked = None
        self._need_cl = True
        self._content_length = None
        self._output = None
        self._input = None
        self._result = None
        self._greenlet = None
        self._sent_bytes = 0

        headers_set = []
        headers_sent = []

        def write(data):
            if not headers_set:
                raise AssertionError("write() before start_response()")

            elif not headers_sent:
                # Before the first output, send the stored headers
                status, response_headers = headers_sent[:] = headers_set
                has_date = has_server = False
                msgs = ['%s %s\r\n' % (environ['SERVER_PROTOCOL'], status)]
                for header in response_headers:
                    msgs.append('%s: %s\r\n' % (header[0], header[1]))
                    name = header[0].lower()
                    if name == 'date':
                        has_date = True
                    elif name == 'server':
                        has_server = True
                if not has_server:
                    msgs.append('Server: Oliver/%s\r\n' % __version__)
                if not has_date:
                    msgs.append('Date: %s\r\n' % _S(format_date_time(time.time())))
                cl = self._content_length
                if cl is None:
                    if self._result is not None:
                        try:
                            n = len(self._result)
                            if n == 1:
                                cl = len(data)
                            elif n == 0 and self._need_cl:
                                cl = 0
                        except:
                            pass
                if self._content_length is not cl:
                    msgs.append('Content-Length: %d\r\n' % cl)
                    self._content_length = cl
                self._chunked = cl is None and self.should_keep_alive() and self._need_cl
                if self._chunked:
                    msgs.append('Transfer-Encoding: chunked\r\n')
                msgs.append('\r\n')

                if self._method == b'HEAD':
                    self._client.sendall(_B(''.join(msgs)))
                elif self._chunked:
                    self._client.sendall(_B(''.join(msgs)))
                else:
                    self.check_content_length(data)
                    data = _B(''.join(msgs)) + data
            else:
                self.check_content_length(data)

            if self._method != b'HEAD':
                if self._chunked:
                    util.write_chunk(self._client, data)
                else:
                    self._client.sendall(data)

        def start_response(status, response_headers, exc_info=None):
            if exc_info:
                try:
                    if headers_sent:
                        # Re-raise original exception if headers sent
                        reraise(exc_info)
                finally:
                    exc_info = None  # avoid dangling circular ref
            elif headers_set:
                raise AssertionError("Headers already set!")

            self._method = self.get_method()
            headers_set[:] = [status, response_headers]
            self._need_cl = not (status.startswith('204') or status.startswith('304') or status.startswith('1'))

            # Note: error checking on the headers should happen here,
            # *after* the headers are set.  That way, if an error
            # occurs, start_response can only be re-called with
            # exc_info set.
            for key, val in response_headers:
                name = key.lower()
                if name in _HOP_BY_HOP_HEADERS:
                    raise AssertionError('Forbidden hop-by-hop header!')
                if name == 'content-length':
                    self._content_length = int(val)
                    if not self._need_cl:
                        if self._content_length != 0:
                            msg = 'Content-Length must be absent or zero for %s response' % status[:3]
                            raise AssertionError(msg)

            return write

        if self.expect_body():
            # has body
            self._output = BodyStream()
            environ['wsgi.input'] = self._input = self._output.get_input()
            self._greenlet = gevent.spawn(self.call_wsgi, environ, start_response, write, headers_sent)
        else:
            self.call_wsgi(environ, start_response, write, headers_sent)

    def call_wsgi(self, environ, start_response, write, headers_sent):
        self._result = result = self._worker.wsgi(environ, start_response)
        try:
            try:
                for data in result:
                    if data:  # don't send headers until body appears
                        write(data)
                if not headers_sent or self._chunked:
                    write(b'')  # send headers now if body was empty or send sentinel if chunked encoding
                if self._content_length is not None and self._sent_bytes < self._content_length and self._method != b'HEAD':
                    raise AssertionError(
                        'Content-Length is %d, but %d bytes sent' % (self._content_length, self._sent_bytes))
            except:
                if headers_sent:
                    util.close(self._client)
                raise
        finally:
            if hasattr(result, 'close'):
                try:
                    result.close()
                except:
                    pass
            if self._output is not None:
                try:
                    self._output.close()
                except:
                    pass
            if not (self.should_keep_alive() or self._content_length is not None or self._chunked):
                self._done = True
                util.close(self._client)

    def on_body(self, data):
        if self._output is not None:
            self._output.get_output().sendall(data)

    def on_message_complete(self):
        if self._output is not None:
            self._output.get_output().close()
        if self._greenlet is not None:
            self._greenlet.get()


class Worker(GeventWorker):
    def __init__(self, *args, **kwargs):
        super(Worker, self).__init__(*args, **kwargs)
        self.wsgi_errors = WSGIErrorsWrapper(self.cfg)

    def handle(self, listener, client, addr):
        protocol = Protocol(self, client, addr, listener.getsockname())
        try:
            try:
                protocol.run()
            except Exception as e:
                self.log.exception('Error handling request')
                self.handle_error(None, client, addr, e)
        finally:
            protocol = None
            util.close(client)
