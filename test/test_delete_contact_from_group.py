from random import randrange
from model.contact import Contact


def test_delete_contact_from_group(app, db):
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Andrew")
    if app.contact.count_contact() == 0:
        app.contact.contact_create(contact)

    select = app.wd.find_element_by_name('group')
    option = select.find_element_by_css_selector("[value='521']")
    option.click()
    if len(app.wd.find_elements_by_name('selected[]')) == 0:
        app.wd.get('http://localhost/addressbook/addressbook/')
        app.contact.select_contact_by_index(index)
        select = app.wd.find_element_by_name("to_group")
        option = select.find_element_by_css_selector("[value='521']")
        option.click()
        app.wd.find_element_by_name("add").click()

    app.wd.get('http://localhost/addressbook/addressbook/')
    select = app.wd.find_element_by_name('group')
    option = select.find_element_by_css_selector("[value='521']")
    option.click()
    contacts_in_group_old = app.wd.find_elements_by_name('selected[]')
    app.wd.find_element_by_name('selected[]').click()
    app.wd.find_element_by_name('remove').click()

    app.wd.find_element_by_link_text('group page "test"').click()
    contacts_in_group_new = app.wd.find_elements_by_name('selected[]')
    assert len(contacts_in_group_new) < len(contacts_in_group_old)


