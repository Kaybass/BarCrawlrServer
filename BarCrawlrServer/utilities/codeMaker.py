from BarCrawlrServer.model.user import user


"""
jankBox is a temporary Island of Misfit Toys for the
functions that exist in utilities that don't have a
place in their own file
"""

def getListOfNamesFromListOfUsers(users):

    names = []

    for k, user in users.items():
        names.append(user.name)

    return names

def createCodeForPlan(plans):

    return ""