import unittest


from BarCrawlrServer.model.plan import plan

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


class Test_planTest(unittest.TestCase):

    def test_plan(self):
        aPlan = plan(json.loads(myPlan))

        self.assertEquals(myPlan,aPlan.jsonify())



if __name__ == '__main__':
    unittest.main()