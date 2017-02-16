import os
import json

from BarCrawlrServer import bcserver

PORT = 7700
DEBUG = False

with open('./settings/settings.json','r') as jsonFile:
    try:
        theJson = json.load(jsonFile)
        PORT = theJson["port"]
        DEBUG = theJson["debug"]
    except(KeyError, json.JSONDecodeError):
        print("WARNING SETTINGS FILE COULD NOT BE LOADED, RUNNING ON DEFAULTS")

if __name__ == '__main__':
    with bcserver.server.app_context():
        bcserver.server.run(debug=DEBUG,port=PORT)