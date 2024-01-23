from model.contact import Contact

def test_update_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.contact_update(Contact(contact_name="Andrew", contact_surname="Suvorov"))
    app.session.logout()