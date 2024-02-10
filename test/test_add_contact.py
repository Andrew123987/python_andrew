from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + ' ' * 10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [  ##[Contact(firstname='', lastname='', address='', homephone='', mobilephone='', workphone='', email='',
    ## email_2='', email_3='')] +

    Contact(firstname=random_string('firstname', 10), lastname=random_string('lastname', 10),
            address=random_string('address', 10), homephone=random_string('homephone', 10),
            mobilephone=random_string('mobilephone', 10),
            workphone=random_string('workphone', 10), email=random_string('email', 10),
            email_2=random_string('email_2', 10), email_3=random_string('email_3', 10))
    for i in range(1)

]


@pytest.mark.parametrize('contact', testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.contact_create(contact)
    assert len(old_contacts) + 1 == app.contact.count_contact()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
