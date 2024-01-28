class GroupHelper:
    def __init__(self, app):
        self.app = app
    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/addressbook/")

    def group_create(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("groups").click()

    def fill_group_form(self, group):
        self.type('group_name', group.name)
        self.type('group_header', group.header)
        self.type('group_footer', group.footer)


    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_xpath("//form[@action='/addressbook/addressbook/group.php']").click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def group_delete(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        wd.find_element_by_link_text("groups").click()



    def group_delete_old(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_xpath("//div[@id='content']/form/span[2]/input").click()
        self.select_first_group()
        wd.find_element_by_name("delete").click()
        wd.find_element_by_link_text("groups").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self,new_group_data):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        self.select_first_group()
        wd.find_element_by_name('edit').click()
        self.fill_group_form(new_group_data)
        wd.find_element_by_name('update').click()