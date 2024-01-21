from fixture.Contact_Helper import ContactHelper
from fixture.Group_Helper import GroupHelper
from fixture.Session_Helper import SessionHelper

class HelperHelper:
    class ContactHelper:
        def __init__(self, app):
            self.app = app

    class GroupHelper:
        def __init__(self, app):
            self.app = app

    class SessionHelper:
        def __init__(self, app):
            self.app = app