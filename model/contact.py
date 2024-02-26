from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, address=None, all_phones_from_home_page=None, homephone=None,
                 mobilephone=None, workphone=None, email=None, all_mailes_from_home_page=None,
                 email_2=None, email_3=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.id = id
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.address = address
        self.email = email
        self.email_2 = email_2
        self.email_3 = email_3
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_mailes_from_home_page = all_mailes_from_home_page

    def __repr__(self):
        return '%s:%s;%s;%s;%s;%s;%s;%s;%s;%s' % (self.id, self.firstname, self.lastname, self.address,
                                                  self.homephone, self.mobilephone, self.workphone,
                                                  self.email, self.email_2, self.email_3)

    def __eq__(self, other):
        return self.firstname == other.firstname and self.lastname == other.lastname and self.address == other.address

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
