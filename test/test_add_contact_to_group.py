from random import randrange
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

from model.contact import Contact


def test_add_contact_to_group(app, db):
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Andrew")
    if app.contact.count_contact() == 0:
        app.contact.contact_create(contact)
    app.contact.select_contact_by_index(index)
    select = app.wd.find_element_by_name("to_group")
    option = select.find_element_by_css_selector("[value='521']")
    option.click()
    app.wd.find_element_by_name("add").click()

    app.open_home_page()
    select = app.wd.find_element_by_name('group')
    option = select.find_element_by_css_selector("[value='521']")
    option.click()
    new_contacts = db.get_contact_list()
    assert len(new_contacts) > 0


