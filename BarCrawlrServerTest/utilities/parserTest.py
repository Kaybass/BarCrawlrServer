import unittest

from BarCrawlrServer.utilities.parser import Parser
from BarCrawlrServer.utilities.logger import Logger
from BarCrawlrServer.model.event import event, eventCodes, events, eventsTypes


#########################################
# A parser to interpret the data from 
#     the logger for the graph.
#########################################
class Test_parserTest(unittest.TestCase):
    def test_A(self):
        evnt = event(eventsTypes[eventCodes.successful_plan_creation]\
                     ,events[eventCodes.successful_plan_creation].format("kek"))

        logger = Logger("kek.txt")

        logger.log(evnt)
        
        prsr = Parser(logger)

        jsonEvent = {
        #self.assertEquals(logger.getLog()[len(logger.getLog()) - 1].replace('\n',''),evnt.toString())
        self.assertEquals(prsr.parse(), jsonEvent)

if __name__ == '__main__':
    unittest.main()
