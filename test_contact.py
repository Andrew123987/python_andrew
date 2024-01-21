# -*- coding: utf-8 -*-

from Contact import Contact
from app import App
import pytest


@pytest.fixture
def app(request):
    fixture = App()
    request.addfinalizer(fixture.stop)
    return fixture


def test_add_contact(app):
        app.login("admin", "secret")
        app.add_new_contact(Contact(contact_name="Andrew", contact_surname="Suvorov"))
        app.logout()
def test_add_empty_contact(app):

        app.login("admin", "secret")
        app.add_new_contact(Contact(contact_name="", contact_surname=""))
        app.logout()











    

    



if __name__ == "__main__":
    unittest.main()
