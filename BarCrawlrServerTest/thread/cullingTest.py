import unittest

from BarCrawlrServer.model.place import place
from BarCrawlrServer.model.plan import plan
from BarCrawlrServer.model.user import user

from BarCrawlrServer.thread.culler import culler

from datetime import datetime

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
        plans["heck"] = plan(myPlan)

        cull = culler(users,plans)

        cull.start() #maybe start(time)?

        users["heck"]["boi"].dateLastTouched = datetime.now - 30

        #sleep(2)

        self.assertEquals(users.exists("heck"),False)

        cull.stop()


if __name__ == '__main__':
    unittest.main()