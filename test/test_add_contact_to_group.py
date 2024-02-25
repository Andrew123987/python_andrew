from random import randrange
from model.contact import Contact


def test_add_contact_to_group(app, db):
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Andrew")
    if app.contact.count_contact() == 0:
        app.contact.contact_create(contact)

    contacts_in_group_before = db.get_contact_in_group()
    app.contact.add_contact_to_group(index)

    contacts_in_group_after = db.get_contact_in_group()
    assert len(contacts_in_group_before) < len(contacts_in_group_after)


