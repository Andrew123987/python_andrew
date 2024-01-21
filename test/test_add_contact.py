from model.Contact import Contact

def test_add_contact(app):
        app.session.login("admin", "secret")
        app.contact.Contact_create(Contact(contact_name="Andrew", contact_surname="Suvorov"))
        app.session.logout()
def test_add_contact_empty(app):
        app.session.login("admin", "secret")
        app.contact.Contact_create(Contact(contact_name="", contact_surname=""))
        app.session.logout()



