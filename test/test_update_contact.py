from model.contact import Contact


def test_update_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(contact_name="Andrew", contact_surname="Suvorov")
    if app.contact.count_contact() == 0:
        app.contact.contact_create(contact)
    app.contact.contact_update(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    contact.id = old_contacts[0].id
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max)
