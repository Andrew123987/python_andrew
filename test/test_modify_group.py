from model.group import Group
from random import randrange


def _modify_some_group(app):
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="test", header="test", footer="test")
    group.id = old_groups[index].id
    if app.group.count() == 0:
        app.group.group_create(group)
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
