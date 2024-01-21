from model.Contact import Contact

def test_update_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.Contact_update(Contact)
    app.session.logout()