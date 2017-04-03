import unittest

from BarCrawlrServer.model.place import place


import json


myPlace = "{" +\
                "\"name\":\"Bob's Bar\"," +\
                "\"address\":\"11 King's Street, Burlington, 05401 VT\"," +\
                "\"lon\":0.1," +\
                "\"lat\":0.1" +\
                "}"

myUser = "{\"name\":\"Alex\",\"lon\":0.0,\"lat\":0.0}"

class Test_placeTest(unittest.TestCase):
    def test_place(self):
        thePlace = place("Bob's Bar","11 King's Street, Burlington, 05401 VT",0.1,0.1)

        self.assertEquals(myPlace,thePlace.jsonify())


if __name__ == '__main__':
    unittest.main()