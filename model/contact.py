from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, contact_address=None, contact_home_phone=None,
                 contact_mobile_phone=None, contact_work_phone=None, contact_fax=None, contact_email_1=None,
                 contact_email_2=None, contact_email_3=None, id=None):
        self.contact_name = firstname
        self.contact_surname = lastname
        self.id = id
        self.contact_home_phone = contact_home_phone
        self.contact_mobile_phone = contact_mobile_phone
        self.contact_work_phone = contact_work_phone
        self.contact_fax = contact_fax
        self.contact_address = contact_address
        self.contact_email_1 = contact_email_1
        self.contact_email_2 = contact_email_2
        self.contact_email_3 = contact_email_3


    def __repr__(self):
        return '%s:%s' % (self.id, self.contact_name)

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id) and self.contact_name == other.contact_name
                and self.contact_surname == other.contact_surname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
