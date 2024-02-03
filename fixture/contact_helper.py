from model.contact import Contact
class ContactHelper:
    def __init__(self, app):
        self.app = app

    def contact_input(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("%s" % contact.contact_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("%s" % contact.contact_surname)


    def contact_create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        wd.get("http://localhost/addressbook/addressbook/edit.php")
        self.contact_input(contact)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()
        self.app.open_home_page()

    def contact_update(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.contact_input(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def contact_delete(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath('//td[8]/a/img').click()
        wd.find_element_by_xpath('//form[2]/input[2]').click()
        self.app.open_home_page()

    def count_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_xpath("//img[@alt='Edit']"))



    def get_contact_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        contacts = []
        for element in wd.find_elements_by_css_selector('td:nth-child(1)'):
            text = element.text
            id = element.find_element_by_name('selected[]').get_attribute('value')
            contacts.append(Contact(contact_name="Andrew", contact_surname="Suvorov", id=id))
        return contacts
