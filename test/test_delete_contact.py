from model.contact import Contact
import random


def _delete_some_contact(app, db, check_ui):
    if app.contact.count_contact() == 0:
        app.contact.contact_create(
            Contact(firstname="Andrew", lastname="Suvorov", homephone='123', mobilephone='456', workphone='789',
                    address='address', email='tst@mail.ru', email_2='tst_2@mail.ru', email_3='tst_3@mail.ru'))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.contact_delete_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                 key=Contact.id_or_max)
    if check_ui:
        new_contacts = map(app.contact.contact_like_on_home_page, db.get_contact_list())
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)



