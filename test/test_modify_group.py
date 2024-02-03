from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.group_create(Group(name='test'))
    app.group.modify_first_group(Group(name="test"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.group_create(Group(name='test'))
    app.group.modify_first_group(Group(header="tst"))


def test_modify_group_footer(app):
    if app.group.count() == 0:
        app.group.group_create(Group(name='test'))
    app.group.modify_first_group(Group(footer="Andrew"))
