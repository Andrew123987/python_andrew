import pytest

from model.group import Group


def test_add_group(app):
    app.group.group_create(Group(name="tst Andrew", header="tst", footer="Andrew"))


def test_add_empty_group(app):
    app.group.group_create(Group(name="", header="", footer=""))


#def test_login_negative(app):
    #app.session.login(username="", password="")

