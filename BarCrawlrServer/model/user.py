import json

from datetime import datetime

"""
 * User is the object used to represent the
 * users using the current plan
 * "name" is a nick created by the user
 * "lon" and "lat" are the user's coords
"""
class user:

    def __init__(self,name,lon,lat):

        self.name = name
        self.lon = float(lon)
        self.lat = float(lat)
        self.dateLastTouched = datetime.now()

    def jsonify(self):

        return '{"name":"' + self.name +\
            '","lon":' + str(self.lon) +\
            ',"lat":' + str(self.lat) + '}'

    def touched(self):
        self.dateLastTouched = datetime.now()

    def getTouched(self):
        return self.dateLastTouched