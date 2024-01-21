# -*- coding: utf-8 -*-

from model.group import Group
from fixture.app import App
import pytest

@pytest.fixture
def app(request):
    fixture = App()
    request.addfinalizer(fixture.stop)
    return fixture

def test_add_group(app):
        app.session.login("admin", "secret")
        app.group.Group_create(Group(name="tst Andrew", header="tst", footer="tst"))
        app.session.logout()

def test_add_empty_group(app):
        app.session.login("admin", "secret")
        app.group.Group_create(Group(name="", header="", footer=""))
        app.session.logout()

def test_login_negative(app):
        app.session.login("X", "X")
        app.session.logout()

