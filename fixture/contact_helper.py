import time

from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def contact_input(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("%s" % contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("%s" % contact.lastname)

    def contact_create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        wd.get("http://localhost/addressbook/addressbook/edit.php")
        self.contact_input(contact)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.app.open_home_page()
        self.contact_cache = None

    def contact_update(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.contact_input(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def contact_update_by_index(self, index, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.contact_input(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def contact_delete(self):
        self.contact_delete_by_index(0)

    def contact_delete_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath('//div[2]/input').click()
        self.app.open_home_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def count_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_xpath("//img[@alt='Edit']"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath('//*[@id="maintable"]//tbody//tr[@name="entry"]'):
                id = element.find_element_by_xpath('.//td[1]//input').get_attribute("value")
                last_name = element.find_element_by_xpath('.//td[2]').text
                first_name = element.find_element_by_xpath('.//td[3]').text
                self.contact_cache.append(Contact(id=id, firstname=first_name, lastname=last_name))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index, contact):
        wd = self.app.wd
        self.contact_update_by_index(index, contact)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        email = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        home = wd.find_element_by_name('home').get_attribute('value')
        mobile = wd.find_element_by_name('mobile').get_attribute('value')
        work = wd.find_element_by_name('work').get_attribute('value')
        fax = wd.find_element_by_name('fax').get_attribute('value')
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                       email=email, email2=email2, email3=email3,
                       home=home, mobile=mobile, work=work, fax=fax)

