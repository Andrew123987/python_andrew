from selenium import webdriver
from fixture.session_helper import SessionHelper
from fixture.group_helper import GroupHelper
from fixture.contact_helper import ContactHelper
from fixture.helper_helper import HelperHelper


class App:
    def __init__(self, browser, base_url, password, username, group_page_url, contact_edit_page):
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.helper = HelperHelper()
        self.base_url = base_url
        self.group_page_url = group_page_url
        self.contact_edit_page = contact_edit_page
        self.browser = browser
        self.password = password
        self.username = username
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError('Unrecognized browser %s' % browser)
        ##options = webdriver.FirefoxOptions()  ## Включение headless режима
        ##options.add_argument('--headless')  ## Включение headless режима
        ##self.wd = webdriver.Firefox(options=options) ## Включение headless режима
        ##self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)
        self.wd.get(base_url)


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith('/addressbook/') and len(
                wd.find_elements_by_class_name('fdTableSortTrigger')) > 0):
            wd.get(self.base_url)

    def open_group_page(self):
        wd = self.wd
        if not (wd.current_url.endswith('/group.php') and len(wd.find_elements_by_name('new')) > 0):
            self.wd.get(self.base_url)

    def stop(self):
        self.wd.quit()
