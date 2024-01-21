# -*- coding: utf-8 -*-

from model.Contact import Contact
from fixture.app import App
import pytest


@pytest.fixture
def app(request):
    fixture = App()
    request.addfinalizer(fixture.stop)
    return fixture


def test_add_contact(app):
        app.session.login("admin", "secret")
        app.contact.Contact_create(Contact(contact_name="Andrew", contact_surname="Suvorov"))
        app.session.logout()
def test_add_contact_empty(app):
        app.session.login("admin", "secret")
        app.contact.Contact_create(Contact(contact_name="", contact_surname=""))
        app.session.logout()











    

    



if __name__ == "__main__":
    unittest.main()
