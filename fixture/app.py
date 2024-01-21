from selenium import webdriver
from fixture.Session_Helper import SessionHelper
from fixture.Group_Helper import GroupHelper
from fixture.Contact_Helper import ContactHelper
from fixture.Helper_Helper import HelperHelper

class App:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.helper = HelperHelper()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/addressbook/")


    def stop(self):
        self.wd.quit()