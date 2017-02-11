import unittest

from BarCrawlrServer.model.place import place
from BarCrawlrServer.model.plan import plan
from BarCrawlrServer.model.user import user

import json

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

myPlace = "{" +\
                "\"name\":\"Bob's Bar\"," +\
                "\"address\":\"11 King's Street, Burlington, 05401 VT\"," +\
                "\"lon\":0.1," +\
                "\"lat\":0.1" +\
                "}"

myUser = "{\"name\":\"Alex\",\"lon\":0.0,\"lat\":0.0}"

class Test_modelTest(unittest.TestCase):
    def test_place(self):
        thePlace = place("Bob's Bar","11 King's Street, Burlington, 05401 VT",0.1,0.1)

        self.assertEquals(myPlace,thePlace.jsonify())

    def test_plan(self):
        aPlan = plan(json.loads(myPlan))

        self.assertEquals(myPlan,aPlan.jsonify())

    def test_user(self):
        aUser = user("Alex",0,0)

        self.assertEquals(myUser,aUser.jsonify())


if __name__ == '__main__':
    unittest.main()
