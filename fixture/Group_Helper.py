class GroupHelper:
    def __init__(self, app):
        self.app = app
    def open_home_page(self):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/addressbook/")

    def Group_create(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_xpath("//form[@action='/addressbook/addressbook/group.php']").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("%s" % group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("%s" % group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("%s" % group.footer)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("groups").click()

    def Group_delete(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_link_text("selected[]").click()
        wd.find_element_by_link_text("delete").click()
        wd.find_element_by_link_text("groups").click()
