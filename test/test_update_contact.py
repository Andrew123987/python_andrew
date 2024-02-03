from model.contact import Contact


def test_update_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count_contact() == 0:
        app.contact.contact_create(Contact(contact_name="Andrew", contact_surname="Suvorov"))
    app.contact.contact_update(Contact(contact_name="Andrew", contact_surname="Suvorov"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
