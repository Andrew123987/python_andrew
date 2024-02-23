from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        wd.get(wd.base_url)

    def open_group_page(self):
        wd = self.app.wd
        wd.get(self.app.group_page_url)

    def group_create(self, group):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_link_text("groups").click()
        self.group_cache = None

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

    def group_delete_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        wd.find_element_by_link_text("groups").click()
        self.group_cache = None

    def group_delete_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        self.select_group_by_id(id)
        wd.find_element_by_name("delete").click()
        wd.find_element_by_link_text("groups").click()
        self.group_cache = None

    def group_delete_first(self):
        self.group_delete_by_index(0)

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value = '%s']" % id).click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        self.select_first_group()
        wd.find_element_by_name('edit').click()
        self.fill_group_form(new_group_data)
        wd.find_element_by_name('update').click()
        self.group_cache = None

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        self.select_group_by_index(index)
        wd.find_element_by_name('edit').click()
        self.fill_group_form(new_group_data)
        wd.find_element_by_name('update').click()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name('selected[]'))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector('span.group'):
                text = element.text
                id = element.find_element_by_name('selected[]').get_attribute('value')
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
