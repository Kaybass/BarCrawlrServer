from BarCrawlrServer.model.user import user

from random import randint


"""
this is a temporary Island of Misfit Toys for the
functions that exist in utilities that don't have a
place in their own file
"""

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getListOfNamesFromListOfUsers(users):

    names = []

    for k, user in users.items():
        names.append(user.name)

    return names

def createCodeForPlan(plans):

    properRun = 0

    code = ""

    while properRun == 0:
        code = ""

        for i in range(0,4):
            code += letters[randint(0, len(letters) -1)]

        if code not in plans.keys():
            properRun = 1

    return code