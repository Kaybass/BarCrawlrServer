import unittest

from BarCrawlrServer.utilities.logger import Logger
from BarCrawlrServer.model.event import event, eventCodes, events, eventsTypes

import json




class Test_loggerTest(unittest.TestCase):
    
    def test_logger(self):
        evnt = event(eventsTypes[eventCodes.successful_plan_creation]\
                     ,events[eventCodes.successful_plan_creation].format("kek"))

        logger = Logger("kek.txt")

        logger.log(evnt)

        self.assertEquals(logger.getLog()[len(logger.getLog()) - 1].replace('\n',''),evnt.toString())


        


if __name__ == '__main__':
    unittest.main()
