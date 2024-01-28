from selenium import webdriver
from fixture.session_helper import SessionHelper
from fixture.group_helper import GroupHelper
from fixture.contact_helper import ContactHelper
from fixture.helper_helper import HelperHelper

#def VisualizationOff(self):
   # self.wd = webdriver.Firefox()
    #self.wd.options = webdriver.FirefoxOptions()
    #self.wd.options.add_argument('--headless')  # Включение headless режима





class App:
    def __init__(self):
        ## self.wd = webdriver.Firefox()
        options = webdriver.FirefoxOptions()  ## Включение headless режима
        options.add_argument('--headless')  ## Включение headless режима
        self.wd = webdriver.Firefox(options=options) ## Включение headless режима
        self.wd.implicitly_wait(30)
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


    def stop(self):
        self.wd.quit()