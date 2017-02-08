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
                "}")\
]

#load settings
APIKEY = "bingobangobongo"
INDEX_MESSAGE = ""

#DEFAULT
PORT = 4000
with open('./settings/settings.json','r') as jsonFile:
    try:
        theJson = json.load(jsonFile)
        APIKEY = theJson["apikey"]
        PORT = theJson["port"]
        INDEX_MESSAGE = theJson["indexMessage"]
    except(KeyError, json.JSONDecodeError):
        print("WARNING SETTINGS FILE COULD NOT BE LOADED, RUNNING ON DEFAULTS")

"""
barcrawlrserver/addplan(apikey)

This target exists so that a client can add a plan to the server

If the plan is valid the server will add the plan to memory, 
create a list of users for that plan and create a code for the
plan. This information will be then sent back to the user.

If the plan is invalid it will return an error
"""
@server.route('/addplan&key=<string:apikey>', methods=['POST'])
def add_plan():
    return "", 201


"""
barcrawlrserver/getplan(code,apikey)

This target allows other clients to connect to a plan that
exists on the server

If the plan exists on the server the client will be sent the
list of users and the plan the code is attached to

If it fails the client will be returned an error
"""
@server.route('/getplan&code=<string:plan_id>&key=<string:apikey>', methods=['GET'])
def get_plan():
    return ""


"""
barcrawlrserver/update(code,nick,apikey,lon,lat)

This target allows clients to send and recieve user
information

The user sends the code of their plan and their
information through url parameters. They get sent
the list of current user information if the plan exists
"""
@server.route('/update&code=<string:plan_id>&nick=<string:user_nick>&key=<string:apikey>' +\
                '&lon=<int:user_lon>&lat=<int:user_lat>', methods=['GET'])
def update_info():
    return ""


"""
barcrawlrserver/disconnect(code,nick,apikey)

This target lets the client disconnect from the list
of active users associated with the plan

If there are no users left connected the plan will be deleted
"""
@server.route('/disconnect&code=<string:plan_id>&nick=<string:user_nick>&key=<string:apikey>', methods=['GET'])
def user_disconnect():
    return ""

@server.route('/')
def index():
    return INDEX_MESSAGE

# 404 Error Handler
@server.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    server.run(port=PORT,debug=True)

#Old stuff
## Post a new plan to the plans list
#@server.route('/plan', methods=['POST'])
#def create_plan():
#    if not request.json or not 'Name' in request.json:
#        abort(400)
#    plans.append(plan(request.json))
#    return jsonify({'plan': plan}), 201

## Get all the plans from the plans list
#@server.route('/plans', methods=['GET'])
#def get_all_plans():
#    s = "All Plans:\n"
#    for plan in plans:
#        s += "\t" + plan.jsonify() + "\n"
#    return s

## Get a specific plan using a plan id number from plans list
#@server.route('/plan&code=<string:plan_id>&key=<string:apikey>',methods=['GET'])
#def get_plan(plan_id,apikey):
#    if len(plans) < plan_id or plan_id < 0:
#        abort(400)
#    return plans[plan_id].jsonify()
