from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Andrew", lastname="Suvorov", homephone='123', mobilephone='456', workphone='789',
                      address='address', email='tst@mail.ru', email_2='tst_2@mail.ru', email_3='tst_3@mail.ru')
    app.contact.contact_create(contact)
    assert len(old_contacts) + 1 == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



