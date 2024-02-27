import re
import time

from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def contact_input(self, contact):
        wd = self.app.wd
        wd.find_element_by_name('firstname').click()
        wd.find_element_by_name('firstname').clear()
        wd.find_element_by_name('firstname').send_keys("%s" % contact.firstname)
        wd.find_element_by_name('lastname').click()
        wd.find_element_by_name('lastname').clear()
        wd.find_element_by_name('lastname').send_keys("%s" % contact.lastname)
        wd.find_element_by_name('home').click()
        wd.find_element_by_name('home').clear()
        wd.find_element_by_name('home').send_keys("%s" % contact.homephone)
        wd.find_element_by_name('mobile').click()
        wd.find_element_by_name('mobile').clear()
        wd.find_element_by_name('mobile').send_keys("%s" % contact.mobilephone)
        wd.find_element_by_name('work').click()
        wd.find_element_by_name('work').clear()
        wd.find_element_by_name('work').send_keys("%s" % contact.workphone)
        wd.find_element_by_name('address').click()
        wd.find_element_by_name('address').clear()
        wd.find_element_by_name('address').send_keys("%s" % contact.address)
        wd.find_element_by_name('email').click()
        wd.find_element_by_name('email').clear()
        wd.find_element_by_name('email').send_keys("%s" % contact.email)
        wd.find_element_by_name('email2').click()
        wd.find_element_by_name('email2').clear()
        wd.find_element_by_name('email2').send_keys("%s" % contact.email_2)
        wd.find_element_by_name('email3').click()
        wd.find_element_by_name('email3').clear()
        wd.find_element_by_name('email3').send_keys("%s" % contact.email_3)

    def contact_create(self, contact, app):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        wd.get(app.contact_edit_page)
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

    def contact_delete_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//div[@id='content']/form[@name='MainForm']/div[2]/input").click()
        self.app.open_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def select_contact_by_id(self, contact):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % contact.id).click()

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
            for element in wd.find_elements_by_name('entry'):
                cells = element.find_elements_by_tag_name('td')
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                id = cells[0].find_element_by_tag_name('input').get_attribute("value")
                all_phones = cells[5].text
                all_mails = cells[4].text
                self.contact_cache.append(Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_mailes_from_home_page=all_mails))

        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.edit_contact(index)
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')
        email = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')
        email3 = wd.find_element_by_name('email3').get_attribute('value')
        homephone = wd.find_element_by_name('home').get_attribute('value').replace(' ', '')
        mobilephone = wd.find_element_by_name('mobile').get_attribute('value').replace(' ', '')
        workphone = wd.find_element_by_name('work').get_attribute('value').replace(' ', '')
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                       email=email, email_2=email2, email_3=email3,
                       homephone=homephone, mobilephone=mobilephone, workphone=workphone)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()

    def edit_contact(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id('content').text
        homephone = re.search('H: (.*)', text).group(1).replace(' ', '')
        mobilephone = re.search('M: (.*)', text).group(1).replace(' ', '')
        workphone = re.search('W: (.*)', text).group(1).replace(' ', '')
        return Contact(homephone=homephone, mobilephone=mobilephone, workphone=workphone)

    def contact_from_home_page(self, contact):
        contact = contact
        firstname = contact.firstname.strip()
        lastname = contact.lastname.strip()
        address = contact.address.strip()
        all_phones = self.merge_phones_like_on_home_page(contact)
        all_emails = self.merge_emails_like_on_home_page(contact)
        return Contact(lastname=lastname, firstname=firstname, id=contact.id,
                       all_phones_from_home_page=all_phones, address=address,
                       all_mailes_from_home_page=all_emails)

    def clear(self, s):
        return re.sub("[() -]", "", s)

    def merge_emails_like_on_home_page(self, contact):
        return '\n'.join(filter(lambda x: x != "" and x is not None, [contact.email, contact.email_2, contact.email_3]))

    def merge_phones_like_on_home_page(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [contact.homephone, contact.mobilephone, contact.workphone]))))

    def filtration_group(self):
        wd = self.app.wd
        select = wd.find_element_by_name('group')
        option = select.find_element_by_css_selector("[value='521']")
        option.click()

    def remove_contact_from_group(self, db, app):
        wd = self.app.wd
        app.open_home_page()
        select = wd.find_element_by_name('group')
        option = select.find_element_by_css_selector("[value='521']")
        option.click()
        contacts_in_group_old = db.get_contact_in_group()
        wd.find_element_by_name('selected[]').click()
        wd.find_element_by_name('remove').click()
        return contacts_in_group_old

    def add_contact_to_group(self, app):
        wd = self.app.wd
        app.open_home_page()
        wd.find_element_by_name('selected[]').click()
        select = wd.find_element_by_name("to_group")
        select.click()
        wd.find_element_by_name("add").click()
        app.open_home_page()

    def update_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        self.contact_input(new_contact_data)
        wd.find_element_by_name("update").click()
        self.app.open_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//div[@id='content']/form[@name='MainForm']/div[2]/input").click()
        self.app.open_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_css_selector('a[href="edit.php?id=%s"]' % id).click()

    def delete_all_contacts(self):
        app = self.app
        if self.app.contact.count_contact() > 0:
            app.open_home_page()
            app.wd.find_element_by_xpath('//input[2]').click()
            app.wd.find_element_by_xpath('//div[2]/input').click()
