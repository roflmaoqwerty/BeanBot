from pony.orm import *
from datetime import datetime

db_name = 'lfg.sqlite'
db = Database()


class Gamerequests(db.Entity):
    requestid = PrimaryKey(int, auto=True)
    user = Required(lambda: Users)
    requesttime = Required(datetime)
    requestduration = Required(int)


class Users(db.Entity):
    userid = PrimaryKey(int, size=64)
    username = Required(str)
    requests = Set(Gamerequests)


def dbinit():
    db.bind(provider='sqlite', filename=db_name, create_db=True)
    db.generate_mapping(create_tables=True)
