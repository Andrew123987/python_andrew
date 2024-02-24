import pymysql
from fixture.orm import ORMFixture

db = ORMFixture(host='127.0.0.1', name='addressbook', user='root', password='')

try:
    l = db.get_group_list()
    for item in l:
        print(l)
    print(len(l))

finally:
    pass
    # db.destroy()
