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

    def __init__(self,aPlan):

        try:

            self.name = aPlan["name"]

            self.places = []
        
            for Place in aPlan["places"]:
                self.places.append(place(Place["name"],\
                                        Place["address"],\
                                        Place["lon"],\
                                        Place["lat"]))

        except(KeyError):
            self.name = "INVALID PLAN"
            self.places = []

    def jsonify(self):

        jsonToReturn = ""

        jsonToReturn += '{"name":"' + self.name + '","places":['
        
        #This segment of code isn't the greatest
        i = 0
        for Place in self.places:
            i += 1
            if i < len(self.places):
                jsonToReturn += Place.jsonify() + ','
            else:
                jsonToReturn += Place.jsonify()

        jsonToReturn += ']}'

        return jsonToReturn
