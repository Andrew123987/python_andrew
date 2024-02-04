from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(contact_name="Andrew", contact_surname="Suvorov")
    app.contact.contact_create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count_contact()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


##def test_add_contact_empty(app):
    ##    old_contacts = app.contact.get_contact_list()
    ##    contact = Contact(contact_name="", contact_surname="")
    ##    app.contact.contact_create(contact)
    ##    new_contacts = app.contact.get_contact_list()
    ##    assert len(old_contacts) + 1 == len(new_contacts)
    ##    old_contacts.append(contact)
##    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
