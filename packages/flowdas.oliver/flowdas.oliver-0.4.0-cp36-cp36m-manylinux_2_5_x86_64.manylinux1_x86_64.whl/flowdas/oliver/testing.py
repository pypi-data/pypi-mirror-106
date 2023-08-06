# coding=utf-8
# Copyright 2017 Flowdas Inc. <prospero@flowdas.com>
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from __future__ import absolute_import

import os

from click.testing import CliRunner as _CliRunner
from falcon import testing

from . import app
from . import base

__all__ = [
    'simulate_command',
    'simulate_request',
    'simulate_delete',
    'simulate_get',
    'simulate_head',
    'simulate_options',
    'simulate_patch',
    'simulate_post',
    'simulate_put',
]


def simulate_command(*args):
    os.environ.setdefault('LC_CTYPE', 'ko_KR.UTF-8')
    runner = _CliRunner()
    return runner.invoke(base.cli, args)


def simulate_request(*args, **kwargs):
    client = testing.TestClient(app.App.wsgi)
    return client.simulate_request(*args, **kwargs)


def simulate_delete(*args, **kwargs):
    return simulate_request('DELETE', *args, **kwargs)


def simulate_get(*args, **kwargs):
    return simulate_request('GET', *args, **kwargs)


def simulate_head(*args, **kwargs):
    return simulate_request('HEAD', *args, **kwargs)


def simulate_options(*args, **kwargs):
    return simulate_request('OPTIONS', *args, **kwargs)


def simulate_patch(*args, **kwargs):
    return simulate_request('PATCH', *args, **kwargs)


def simulate_post(*args, **kwargs):
    return simulate_request('POST', *args, **kwargs)


def simulate_put(*args, **kwargs):
    return simulate_request('PUT', *args, **kwargs)
