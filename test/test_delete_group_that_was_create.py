from model.group import Group
def test_delete_group_that_was_create(app):
    if app.group.count() == 0:
        app.group.group_create(Group(name='test'))
    app.group.group_delete_old()
