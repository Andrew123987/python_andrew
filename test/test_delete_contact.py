from model.contact import Contact
import random


def test_delete_some_contact(app, db, check_ui):
    old_contacts = db.get_contact_list()
    app.contact.contact_create(
        Contact(firstname="Andrew", lastname="Suvorov", homephone='123', mobilephone='456', workphone='789',
                address='address', email='tst@mail.ru', email_2='tst_2@mail.ru', email_3='tst_3@mail.ru'), app)
    contact = random.choice(old_contacts)
    app.contact.contact_delete_by_id()
    new_contacts = db.get_contact_list()
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                 key=Contact.id_or_max)
    assert old_contacts == new_contacts
    if check_ui:
        new_contacts = map(app.contact.contact_like_on_home_page, db.get_contact_list())
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
