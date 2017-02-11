from BarCrawlrServer.model.user import user
from BarCrawlrServer.model.plan import plan


def createUsersJsonFromDict(users):
    json = '{"users":['

    i = 0
    for key, User in users.items():
        i += 1
        if i < len(users.items()):
            json += User.jsonify() + ','
        else:
            json += User.jsonify()

    json += ']}'

    return json

def createGetPlanJson(aPlan,users):

    json = '{"plan":"'

    json += aPlan.jsonify()

    json += ',"users":' + createUsersJsonFromDict(users)

    json += '}'

    return json

def createAddPlanJson(code,aPlan,users):
    return ""