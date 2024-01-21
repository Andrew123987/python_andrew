from model.Contact import Contact

def test_delete_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.Contact_delete(Contact)
    app.session.logout()