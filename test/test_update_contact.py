from model.contact import Contact


def test_update_contact(app):
    if app.contact.count_contact() == 0:
        app.contact.contact_create(Contact(contact_name="Andrew", contact_surname="Suvorov"))
    app.contact.contact_update(Contact(contact_name="Andrew", contact_surname="Suvorov"))
