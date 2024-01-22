def test_update_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.group_update()
    app.session.logout()