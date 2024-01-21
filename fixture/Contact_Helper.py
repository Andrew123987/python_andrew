
class ContactHelper:
    def __init__(self, app):
        self.app = app

    def Contact_create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        wd.get("http://localhost/addressbook/addressbook/edit.php")
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("%s" % contact.contact_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("%s" % contact.contact_surname)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()