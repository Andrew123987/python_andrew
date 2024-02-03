from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.contact_create(Contact(contact_name="Andrew", contact_surname="Suvorov"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)


def test_add_contact_empty(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.contact_create(Contact(contact_name="", contact_surname=""))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
