def test_delete_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.contact_delete()
    app.session.logout()