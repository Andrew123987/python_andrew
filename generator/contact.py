from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], 'n:f:', ['number of contacts', 'file'])
except getopt.GetoptError as err:
    print(
        "Генератор запускать так:\npython contact.py -n <количество контактов> -f <файл, в который будут сохранены "
        "данные>")
    sys.exit(2)
n = 5
f = 'data/contacts.json'

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + ' ' * 10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname='Andrew1', lastname='test1', address='street1', homephone='123', mobilephone='456',
            workphone='789',
            email='test1@mail.ru', email_2='test2@mail.ru', email_3='test3@mail.ru'),
    Contact(firstname='Andrew2', lastname='test2', address='street2', homephone='321', mobilephone='654',
            workphone='987',
            email='test11@mail.ru', email_2='test22@mail.ru', email_3='test3@mail.ru')

]

# testdata = [
#    Contact(firstname=random_string('firstname', 10), lastname=random_string('lastname', 10),
#            address=random_string('address', 10), homephone=random_string('homephone', 10),
#            mobilephone=random_string('mobilephone', 10),
#            workphone=random_string('workphone', 10), email=random_string('email', 10),
#            email_2=random_string('email_2', 10), email_3=random_string('email_3', 10))
#    for i in range(n)

# ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options('json', indent=2)
    out.write(jsonpickle.encode(testdata))
