# -*- coding: utf-8 -*-

from django_webtest import DjangoTestApp, WebTestMixin
import pytest


@pytest.fixture(scope='function')
def app(request):
    wtm = WebTestMixin()
    wtm._patch_settings()
    wtm._disable_csrf_checks()
    request.addfinalizer(wtm._unpatch_settings)

    return DjangoTestApp()
