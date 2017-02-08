import json
import sys

from flask import Flask, jsonify, current_app, make_response, abort

from BarCrawlrServer.model.plan import plan



server = Flask(__name__)

#Example plan data we will throw out eventually
plans = [
    plan("{" +\
                "\"name\":\"Alex's Plan\"," +\
                "\"places\":[" +\
                "{" +\
                "\"name\":\"Joe's Bar\"," +\
                "\"address\":\"10 King's Street, Burlington, 05401 VT\"," +\
                "\"lon\":0.0," +\
                "\"lat\":0.0" +\
                "}," +\
                "{" +\
                "\"name\":\"Bob's Bar\"," +\
                "\"address\":\"11 King's Street, Burlington, 05401 VT\"," +\
                "\"lon\":0.1," +\
                "\"lat\":0.1" +\
                "}" +\
                "]" +\
                "}"),\
    plan('{"Name":"test_plan_2","Address":"Oceanic location","Location":[0,0],"Note":"Second test plan for testing"}')
]

#load settings
APIKEY = ""

#DEFAULT
PORT = 4000
with open('./settings/settings.json','r') as jsonFile:
    try:
        theJson = json.load(jsonFile)
        APIKEY = theJson["apikey"]
        PORT = theJson["port"]
    except(KeyError, json.JSONDecodeError):
        sys.exit("Settings file could not be loaded properly.")

@server.route('/')
def index():
    return "Welcome to Bar Crawlr Server"

# Post a new plan to the plans list
@server.route('/plan', methods=['POST'])
def create_plan():
    if not request.json or not 'Name' in request.json:
        abort(400)
    plans.append(plan(request.json))
    return jsonify({'plan': plan}), 201

# Get all the plans from the plans list
@server.route('/plans', methods=['GET'])
def get_all_plans():
    s = "All Plans:\n"
    for plan in plans:
        s += "\t" + plan.jsonify() + "\n"
    return s

# Get a specific plan using a plan id number from plans list
@server.route('/plan&code=<int:plan_id>&key=<string:apikey>',methods=['GET'])
def get_plan(plan_id,apikey):
    if len(plans) < plan_id or plan_id < 0:
        abort(400)
    return plans[plan_id].jsonify()

# 404 Error Handler
@server.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    server.run(port=PORT,debug=True)
