import beanbot.db.dbschema as beanscheme
from pony.orm import *

@db_session
def user_exists(userid):
    user = beanscheme.Users.get(userid=userid)
    if user is None:
        return False
    else:
        return True


@db_session
def add_user(userid, username):
    new_user = beanscheme.Users(userid=userid, username=username)
    return new_user
