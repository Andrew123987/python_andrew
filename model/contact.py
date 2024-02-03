from sys import maxsize


class Contact:
    def __init__(self, contact_name=None, contact_surname=None, id=None):
        self.contact_name = contact_name
        self.contact_surname = contact_surname
        self.id = id

    def __repr__(self):
        return '%s:%s' % (self.id, self.contact_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.contact_name == other.contact_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
