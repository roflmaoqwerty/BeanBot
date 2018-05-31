import beanbot.db.dbschema as beanscheme
from datetime import datetime
from pony.orm import *


@db_session
def add_request(user, duration):
    requesttime = datetime.utcnow()
    new_request = beanscheme.Gamerequests(user=user, requesttime=requesttime, requestduration=duration)
    return new_request
