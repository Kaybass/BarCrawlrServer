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

        try:
            plan = json.loads(thePlan)

            self.name = plan["name"]

            self.places = []
        
            for Place in plan["places"]:
                self.places.append(place(Place["name"],\
                                        Place["address"],\
                                        Place["lon"],\
                                        Place["lat"]))

        except(KeyError, json.JSONDecodeError):
            self.name = "INVALID PLAN"
            self.places = []

    def jsonify(self):

        jsonToReturn = ""

        jsonToReturn += '{"name":"' + self.name + '","places":['

        for Place in self.places:
            jsonToReturn += Place.jsonify() + ','

        jsonToReturn += ']}'

        return jsonToReturn
                
