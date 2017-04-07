import unittest

from BarCrawlrServer.model.user import user
from BarCrawlrServer.model.plan import plan

import BarCrawlrServer.utilities.barJsons as bjs

import json

"""

Joe please write please

"""

class barJsonsTest(unittest.TestCase):

    def test_userJson(self):

        users = {1:user("Alex", 1, 2),2:user("Joe", 3, 4)}
        
        resultJSON = bjs.createUsersJsonFromDict(users)

        expectedJSON = '{"users":[{"name":"Alex","lon":1.0,"lat":2.0},{"name":"Joe","lon":3.0,"lat":4.0}]}'

        self.assertEquals(resultJSON, expectedJSON)

    def test_getPlan(self):
        
        myPlan = "{" +\
                "\"name\":\"Alex's Plan\"," +\
                "\"places\":[" +\
                "{" +\
                "\"name\":\"Joe's Bar\"," +\
                "\"address\":\"10 King's Street, Burlington, 05401 VT\"," +\
                "\"lon\":0.0," +\
                "\"lat\":0.0" +\
                "}," +\
                "{" +\
                "\"name\":\"Bob's Bar\"," +\
                "\"address\":\"11 King's Street, Burlington, 05401 VT\"," +\
                "\"lon\":0.1," +\
                "\"lat\":0.1" +\
                "}" +\
                "]" +\
                "}"

        aPlan = plan(json.loads(myPlan))

        users = {1:user("Alex", 1, 2),2:user("Joe", 3, 4)}
        
        resultJSON = bjs.createGetPlanJson(aPlan, users)

        expectedJSON = '{"plan":{"name":"Alex\'s Plan","places":[{"name":"Joe\'s Bar","address":"10 King\'s Street, Burlington, 05401 VT","lon":0.0,"lat":0.0},{"name":"Bob\'s Bar","address":"11 King\'s Street, Burlington, 05401 VT","lon":0.1,"lat":0.1}]},"users":{"users":[{"name":"Alex","lon":1.0,"lat":2.0},{"name":"Joe","lon":3.0,"lat":4.0}]}}'

        self.assertEquals(resultJSON, expectedJSON)

    def test_addPlan(self):

        myPlan = "{" +\
                "\"name\":\"Alex's Plan\"," +\
                "\"places\":[" +\
                "{" +\
                "\"name\":\"Joe's Bar\"," +\
                "\"address\":\"10 King's Street, Burlington, 05401 VT\"," +\
                "\"lon\":0.0," +\
                "\"lat\":0.0" +\
                "}," +\
                "{" +\
                "\"name\":\"Bob's Bar\"," +\
                "\"address\":\"11 King's Street, Burlington, 05401 VT\"," +\
                "\"lon\":0.1," +\
                "\"lat\":0.1" +\
                "}" +\
                "]" +\
                "}"

        aPlan = plan(json.loads(myPlan))

        users = {1:user("Alex", 1, 2),2:user("Joe", 3, 4)}

        resultJSON = bjs.createAddPlanJson('1234',aPlan,users);

        print(resultJSON)

        expectedJSON = '{"code":"1234","plan":{"name":"Alex\'s Plan","places":[{"name":"Joe\'s Bar","address":"10 King\'s Street, Burlington, 05401 VT","lon":0.0,"lat":0.0},{"name":"Bob\'s Bar","address":"11 King\'s Street, Burlington, 05401 VT","lon":0.1,"lat":0.1}]},"users":{"users":[{"name":"Alex","lon":1.0,"lat":2.0},{"name":"Joe","lon":3.0,"lat":4.0}]}}'

        self.assertEquals(resultJSON, expectedJSON)

if __name__ == '__main__':
    unittest.main()