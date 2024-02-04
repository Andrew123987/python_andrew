from model.contact import Contact
from random import randrange

def test_delete_some_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count_contact() == 0:
        app.contact.contact_create(Contact(contact_name="Andrew", contact_surname="Suvorov"))
    index = randrange(len(old_contacts))
    app.contact.contact_delete_by_index(index)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
