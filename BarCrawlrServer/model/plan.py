import json
from BarCrawlrServer.model.place import place


"""
 * Plan is the object that the client uses
 * to organize their bar crawling experience
 * "name" is the name of the plan (i.e "Bob's Birthday")
 * "places" are the locations that are in the plan
 * @see Place
"""
class plan:

    def __init__(self,thePlan):

        plan = json.loads(thePlan)

        self.name = plan["name"]
        
        for Place in plan["places"]:
            self.places.append(Place)

    def jsonify(self):

        jsonToReturn = ""

        jsonToReturn += '{"name
                
