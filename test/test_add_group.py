import pytest
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.group_create(Group(name="tst Andrew", header="tst", footer="Andrew"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_add_empty_group(app):
    app.group.group_create(Group(name="", header="", footer=""))

