from model.contact import Contact
from random import randrange


def _update_some_contact(app, db, check_ui):
    if app.contact.count_contact() == 0:
        app.contact.create(Contact(firstname="Andrew", lastname="Suvorov", address="street"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Andrew", lastname="Suvorov", address="street" + str(index))
    contact.id = old_contacts[index].id
    contact.lastname = old_contacts[index].lastname
    app.contact.update_contact_by_id(contact.id, contact)
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        new_contacts = map(app.contact.contact_like_on_home_page, db.get_contact_list())
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

