from model.contact import Contact

def test_add_contact(app):
        app.contact.contact_create(Contact(contact_name="Andrew", contact_surname="Suvorov"))

def test_add_contact_empty(app):
        app.contact.contact_create(Contact(contact_name="", contact_surname=""))




