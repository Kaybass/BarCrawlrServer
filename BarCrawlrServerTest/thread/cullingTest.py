import unittest

from BarCrawlrServer.model.place import place
from BarCrawlrServer.model.plan import plan
from BarCrawlrServer.model.user import user

from BarCrawlrServer.thread.culler import userCull

from datetime import datetime, timedelta

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

class Test_cullingTest(unittest.TestCase):
    
    def test_culler(self):

        users = {}
        plans = {}

        users["heck"] = {"boi" : user("boi",60,80)}
        plans["heck"] = plan(json.loads(myPlan))

        
        users["heck"]["boi"].dateLastTouched = datetime.now() - timedelta(hours=10)

        userCull(users,plans)

        #sleep(2)

        self.assertEquals('heck' in users.keys(),False)

        


if __name__ == '__main__':
    unittest.main()