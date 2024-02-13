import re


def test_all_contacts_info(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index=0)
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    assert clear(contact_from_home_page.firstname) == clear(contact_from_edit_page.firstname)
    assert clear(contact_from_home_page.lastname) == clear(contact_from_edit_page.lastname)
    assert clear(contact_from_home_page.address) == clear(contact_from_edit_page.address)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_mailes_from_home_page == merge_mails_like_on_home_page(contact_from_edit_page)


def merge_phones_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x != '',
                            map(lambda x: clear(x), filter(lambda x: x is not None,
                                                           [contact.homephone, contact.mobilephone,
                                                            contact.workphone]))))


def merge_mails_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x != '',
                            map(lambda x: x, filter(lambda x: x is not None,
                                                          [contact.email, contact.email_2,
                                                           contact.email_3]))))


def clear(s):
    return re.sub('[() -]', '', s)
