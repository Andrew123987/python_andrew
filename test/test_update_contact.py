from model.contact import Contact
from random import randrange

def test_update_some_contact(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Andrew", lastname="Suvorov", homephone='123', mobilephone='456', workphone='789', address='address',
                       email='tst@mail.ru', email_2='tst_2@mail.ru', email_3='tst_3@mail.ru')
    if app.contact.count_contact() == 0:
        app.contact.contact_create(contact)
    app.contact.contact_update_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    contact.id = old_contacts[index].id
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max)
