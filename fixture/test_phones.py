def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index=0)
    assert contact_from_home_page.contact_name == contact_from_edit_page.contact_name
    assert contact_from_home_page.contact_surname == contact_from_edit_page.contact_surname
    assert contact_from_home_page.contact_address == contact_from_edit_page.contact_address
    assert contact_from_home_page.contact_home_phone == contact_from_edit_page.contact_home_phone
    assert contact_from_home_page.contact_mobile_phone == contact_from_edit_page.contact_mobile_phone
    assert contact_from_home_page.contact_work_phone == contact_from_edit_page.contact_work_phone
    assert contact_from_home_page.contact_address == contact_from_edit_page.contact_address
    assert contact_from_home_page.contact_email_1 == contact_from_edit_page.contact_email_1
    assert contact_from_home_page.contact_email_2 == contact_from_edit_page.contact_email_2
    assert contact_from_home_page.contact_email_3 == contact_from_edit_page.contact_email_3

