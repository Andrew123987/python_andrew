class SessionHelper:
    def __init__(self, app):
        self.app = app


    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def logout(self):
        wd = self.app. wd
        wd.find_element_by_link_text("Logout").click()
        #wd.quit()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text('Logout')) > 0

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element_by_xpath("//div[@id='top']/form/b").text == '('+username+')'

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in_as(username):
            return
        else:
            self.logout()
        self.login(self, username, password)

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/addressbook/') and len(wd.find_elements_by_class_name('fdTableSortTrigger')) > 0):
            wd.get("http://localhost/addressbook/addressbook/")