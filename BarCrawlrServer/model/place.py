import json

"""
 * Place is an object that represents the places
 * users plan to go during a bar crawl.
 * "name" is the name of the location
 * "address" is the street address of the location
 * "lon" and "lat" are the coords
"""
class place:
    
    def __init__(self, name, address, lon, lat):

        self.name = name
        self.address = address
        self.lon = lon
        self.lat = lat

    def jsonify(self):

        return '{"name":"' + self.name +\
            '","address":"' + self.address +\
            '","lon":' + str(self.lon) +\
            ',"lat":' + str(self.lat) + '}'
        

