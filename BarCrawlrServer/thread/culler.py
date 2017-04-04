from BarCrawlrServer.model.plan import plan
from BarCrawlrServer.model.user import user

from datetime import datetime, timedelta

def userCull(Users, plans):
    Thing1 = Users.copy()
    for key, User in Thing1.items():
        Thing2 = User.copy()
        for key2, User2 in Thing2.items():
            if (User2.getTouched() + timedelta(hours=1)) < datetime.now():
                del Users[key][key2]
        if len(Users[key]) == 0:
            del plans[key]
            del Users[key]