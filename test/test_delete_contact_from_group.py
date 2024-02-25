from random import randrange
from model.contact import Contact


def test_delete_contact_from_group(app, db):
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Andrew")
    if app.contact.count_contact() == 0:
        app.contact.contact_create(contact)

    app.contact.filtration_group_521()
    if len(app.wd.find_elements_by_name('selected[]')) == 0:
        app.contact.add_contact_to_group_521(index)

    contacts_in_group_old = app.contact.remove_contact_from_group_521(db)

    app.wd.find_element_by_link_text('group page "test"').click()
    contacts_in_group_new = db.get_contact_in_group()
    assert len(contacts_in_group_new) < len(contacts_in_group_old)





