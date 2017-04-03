import unittest

from BarCrawlrServer.model.user import user

import json


myUser = "{\"name\":\"Alex\",\"lon\":0.0,\"lat\":0.0}"

class Test_userTest(unittest.TestCase):

    def test_user(self):
        aUser = user("Alex",0,0)

        self.assertEquals(myUser,aUser.jsonify())


if __name__ == '__main__':
    unittest.main()