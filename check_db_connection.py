import pymysql
from fixture.db import DbFixture

db = DbFixture(host='127.0.0.1', name='addressbook', user='root', password='')

try:
    groups = db.get_group_list()
    for group in groups:
        print(groups)
    print(len(groups))

finally:
    db.destroy()
