from model.contact import Contact


def test_add_contact_to_group(app, db):
    contacts_in_group_before = db.get_contact_in_group()

    contact = Contact(firstname="Andrew")
    app.contact.contact_create(contact, app)

    app.contact.add_contact_to_group(contact, app)

    contacts_in_group_after = db.get_contact_in_group()
    assert len(contacts_in_group_before) < len(contacts_in_group_after)
