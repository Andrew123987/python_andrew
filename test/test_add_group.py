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
        app.login("admin", "secret")
        app.add_element_in_address_book(Group(name="tst Andrew", header="tst", footer="tst"))
        app.logout()

def test_add_empty_group(app):
        app.login("admin", "secret")
        app.add_element_in_address_book(Group(name="", header="", footer=""))
        app.logout()

def test_login_negative(app):
        app.login("X", "X")
        app.logout()

