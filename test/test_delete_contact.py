from model.contact import Contact


def test_delete_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count_contact() == 0:
        app.contact.contact_create(Contact(contact_name="Andrew", contact_surname="Suvorov"))
    app.contact.contact_delete()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
