# coding=utf-8
# Copyright 2017 Flowdas Inc. <prospero@flowdas.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from __future__ import absolute_import

import falcon

from .openapi import OpenAPI

__all__ = [
    'App',
    'Request',
]


class Request(falcon.Request):
    """:py:class:`falcon.Request` 를 대체한다.

    잘못된 형식의 쿠키가 올라오는 경우 :py:class:`falcon.Request` 가 다른 쿠키까지 잃어버리는 문제를 해결한다.

    :py:class:`App` 를 사용하면 자동 적용된다.

    Since version 0.3.
    """
    __slots__ = ()

    @property
    def cookies(self):
        if self._cookies is None:
            cookietxt = self.get_header('Cookie')
            cookies = {}
            if cookietxt:
                for cook in cookietxt.split(';'):
                    cook = cook.lstrip()
                    try:
                        k, v = cook.split('=', 1)
                        if v.startswith('"') and v.endswith('"'):
                            v = v[1:-1]
                        cookies[k] = v
                    except ValueError:
                        pass
            self._cookies = cookies

        return self._cookies.copy()


class App(falcon.API):
    """:py:class:`falcon.API` 을 대체한다.

    다중 호스트를 지원하고, 호스트 별로 별도의 App 인스턴스가 만들어진다. host 별로 singleton 이 유지된다.

    :py:class:`falcon.API` 를 계승하는 클래스이며, :py:class:`falcon.API` 가 받아들이는 모든 키워드 인자들을 지원하고,
    추가로 다음과 같은 인자를 지원한다.

    host
        App 이 연결될 호스트명. 생략하면 '*' 가 적용되고, default App 으로 사용된다.

    Since version 0.3.
    """
    _instances = {}
    _default = None

    __slots__ = ('_host', '_ops', '_oass')

    def __new__(cls, host='*'):
        host = host.lower()
        instance = App._default if host == '*' else App._instances.get(host)
        if instance is None:
            instance = super(App, cls).__new__(cls)
            if host == '*':
                App._default = instance
            else:
                App._instances[host] = instance
        return instance

    def __init__(self, host='*', **kwargs):
        # 오직 한번만 __init__ 가 호출되어야 한다.
        if not hasattr(self, '_host'):
            kwargs.setdefault('request_type', Request)
            super(App, self).__init__(**kwargs)
            self._host = host.lower()
            self._ops = {}
            self._oass = []

    @staticmethod
    def wsgi(env, start_response):
        host = env.get('HTTP_HOST') or ''
        app = App._instances.get(host.lower()) or App._default
        if app:
            return app(env, start_response)
        else:
            start_response('404 Not Found', [])
            return []

    @staticmethod
    def invoke_ready(func):
        if App._default is None and not App._instances:
            # 최소한 하나의 App 인스턴스는 제공되어야 한다.
            App()
        if App._default:
            func(App._default)
        for app in App._instances.values():
            func(app)

    @property
    def host(self):
        """연결된 호스트 이름.

        '*' 는 default.

        Since version 0.3.
        """
        return self._host

    def add_openapi(self, oas):
        """OpenAPI Specification(OAS) 명세로 정의된 인터페이스를 만든다.

        operationId 가 선언되지 않았거나, 구현이 제공되지 않으면, 해당 요청은 ``501 Not Implemented`` 로 응답한다.

        oas
            ``dict`` 형으로 제공되는 OAS 명세.

        Since version 0.4.
        """
        oas = OpenAPI().load(oas)
        oas.install(self)
        self._oass.insert(0, oas)

    def operation(self, func):
        """OAS 명세에서 선언한 operationId 와 구현을 연결하는데 사용되는 데코레이터.

        함수의 이름이 operationId 로 사용된다.

        :py:meth:`add_oas` 와의 순서는 상관없다. 선언되지 않은 operationId 를 제공하면 무시된다.

        Example:

            >>> app = oliver.App()
            >>>
            >>> @app.operation
            ... def get_books(self, request, response):
            ...     r = response(200)
            ...     item = r.type.item().update(id='9780141439747', title='Oliver Twist')
            ...     r.body.append(item)
            ...     return r

        Since version 0.4.
        """
        self._ops[func.__name__] = func
        return func
