from sys import maxsize


class Contact:
    def __init__(self, firstname=None, lastname=None, address=None, homephone=None,
                 mobilephone=None, workphone=None, email=None,
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

    def __repr__(self):
        return '%s:%s' % (self.id, self.firstname)

    def __eq__(self, other):
        return ((self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname
                and self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
