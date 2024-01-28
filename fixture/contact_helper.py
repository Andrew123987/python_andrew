
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

    def contact_update(self, contact):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/addressbook/")
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.contact_input(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def contact_delete(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/addressbook/")
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()

    def count_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_xpath("//img[@alt='Edit']"))
