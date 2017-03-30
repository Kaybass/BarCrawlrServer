import unittest

from BarCrawlrServer.utilities.logger import logger
from BarCrawlrServer.model.event import event

import json



class Test_loggerTest(unittest.TestCase):
    
    def test_logger(self):
        evnt = new event("A thing happened")

        logger().log(evnt)

        strn = logger().getLog()

        self.assertEquals(strn,"A thing happened")


if __name__ == '__main__':
    unittest.main()
