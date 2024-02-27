import uuid
from model.contact import Contact


def test_delete_contact_from_group(app, db):
    a = str(uuid.uuid4())
    contact = Contact(firstname="Andrew" + a, lastname="Suvorov" + a, address="street" + a, workphone=a, mobilephone=a,
                      homephone=a,
                      email=a + "@mail.ru", email_2=a + "@mail.ru", email_3=a + "@mail.ru")

    # применил новый метод, так как пересмотрел подход к тестам, исходя из реального рабочего опыта
    app.contact.delete_all_contacts()
    app.contact.contact_create(contact, app)
    app.contact.add_contact_to_group(app)
    contacts_in_group_before = db.get_contact_in_group()
    app.contact.remove_contact_from_group(app)
    contacts_in_group_after = db.get_contact_in_group()
    assert len(contacts_in_group_before) > len(contacts_in_group_after)
