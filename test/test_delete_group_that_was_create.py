def test_delete_group_that_was_create(app):
    app.session.login(username="admin", password="secret")
    app.group.group_delete_old()
    app.session.logout()