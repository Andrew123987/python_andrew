from model.group import Group


def _add_group(app, db, json_groups):
    group = json_groups
    old_groups = db.get_group_list()
    app.group.group_create(group)
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
