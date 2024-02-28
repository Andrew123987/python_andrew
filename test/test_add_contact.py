from model.contact import Contact


def test_add_contact(app, db, json_contacts, check_ui):
    old_contacts = db.get_contact_list()
    contact = json_contacts
    app.contact.contact_create(contact, app)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    assert old_contacts == new_contacts
    if check_ui:
        new_contacts = map(app.contact.contact_like_on_home_page, db.get_contact_list())
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)