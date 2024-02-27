from random import randrange
from model.contact import Contact


def _delete_contact_from_group(app, db):
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Andrew")
    if app.contact.count_contact() == 0:
        app.contact.contact_create(contact)

    app.contact.filtration_group()
    if len(app.wd.find_elements_by_name('selected[]')) == 0:
        app.contact.add_contact_to_group(index, app)

    contacts_in_group_before = app.contact.remove_contact_from_group(db, app)
    contacts_in_group_after = db.get_contact_in_group()
    assert len(contacts_in_group_before) > len(contacts_in_group_after)





