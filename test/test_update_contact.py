def test_update_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.contact_update()
    app.session.logout()