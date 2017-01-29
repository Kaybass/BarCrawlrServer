import json


class plan:


    def __init__(self,thePlan):
        
        Plan = json.loads(thePlan)

        self.name = Plan["Name"]

        self.address = Plan["Address"]

        self.lat = Plan["Location"][0]

        self.lon = Plan["Location"][1]

        self.note = Plan["Note"]

    def jsonify(self):

                return "Plan Name: " + self.name + \
                 ", Address: " + self.address +\
                 ", Location: [" + str(self.lat) + \
                ", " + str(self.lon) + "], Notes: " + self.note
