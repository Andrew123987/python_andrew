import random
from model.group import Group


def test_delete_some_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.group_create(Group(name='test'))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.group_delete_by_id(group.id)
    new_groups = db.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    # assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
