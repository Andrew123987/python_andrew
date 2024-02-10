import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index=0)
    assert contact_from_home_page.firstname == clear(contact_from_edit_page.firstname)
    assert contact_from_home_page.lastname == clear(contact_from_edit_page.lastname)
    assert contact_from_home_page.address == clear(contact_from_edit_page.address)
    assert contact_from_home_page.homephone == clear(contact_from_edit_page.homephone)
    assert contact_from_home_page.mobilephone == clear(contact_from_edit_page.mobilephone)
    assert contact_from_home_page.workphone == clear(contact_from_edit_page.workphone)
    assert contact_from_home_page.email == clear(contact_from_edit_page.email)
    assert contact_from_home_page.email_2 == clear(contact_from_edit_page.email_2)
    assert contact_from_home_page.email_3 == clear(contact_from_edit_page.email_3)


def test_phones_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    ##assert contact_from_view_page.firstname == contact_from_edit_page.firstname
    ##assert contact_from_view_page.lastname == contact_from_edit_page.lastname
    ##assert contact_from_view_page.address == contact_from_edit_page.address
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    ##assert contact_from_view_page.email == contact_from_edit_page.email
    ##assert contact_from_view_page.email_2 == contact_from_edit_page.email_2
    ##assert contact_from_view_page.email_3 == contact_from_edit_page.email_3

def clear(s):
    return re.sub('[() -]', '', s)
