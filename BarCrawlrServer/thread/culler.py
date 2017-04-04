from BarCrawlrServer.model.plan import plan
from BarCrawlrServer.model.user import user

def userCull(users, plans):
    for key, User in Users.items():
        for key2, User2 in User.items():
            if (User2.getTouched() + datetime.timedelta(hours=1)) < datetime.now():
                del Users[key2]
        if len(plans[key]) == 0:
            del plans[key]
    return