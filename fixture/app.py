from selenium import webdriver
from fixture.session_helper import SessionHelper
from fixture.group_helper import GroupHelper
from fixture.contact_helper import ContactHelper
from fixture.helper_helper import HelperHelper

class App:
    def __init__(self):
        options = webdriver.FirefoxOptions()  ## Включение headless режима
        options.add_argument('--headless')  ## Включение headless режима
        self.wd = webdriver.Firefox(options=options) ## Включение headless режима
        self.wd.implicitly_wait(5)
        self.wd.get("http://localhost/addressbook/addressbook/")
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.helper = HelperHelper()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/addressbook/")

    def open_group_page(self):
        wd = self.wd
        if not (wd.current_url.endswith('/group.php') and len(wd.find_elements_by_name('new')) > 0):
            wd.get('http://localhost/addressbook/addressbook/group.php')

    def stop(self):
        self.wd.quit()