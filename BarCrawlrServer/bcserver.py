import json

import BarCrawlrServer.utilities.barJsons as barJsons
import BarCrawlrServer.utilities.codeMaker as cm

from flask import Flask, jsonify, current_app, make_response, abort, request

from BarCrawlrServer.model.plan import plan
from BarCrawlrServer.model.user import user

import json

server = Flask(__name__)

#Dictionaries to store plan and user data
plans = {}
users = {}

#DEFAULT SETTINGS
APIKEY = "bingobangobongo"
INDEX_MESSAGE = ""

#load settings
with open('./settings/settings.json','r') as jsonFile:
    try:
        theJson = json.load(jsonFile)
        APIKEY = theJson["apikey"]
        INDEX_MESSAGE = theJson["indexMessage"]
    except(KeyError, json.JSONDecodeError):
        print("WARNING SETTINGS FILE COULD NOT BE LOADED, RUNNING ON DEFAULTS")


"""
barcrawlrserver/addplan(apikey,nick,lon,lat)

This target exists so that a client can add a plan to the server

If the plan is valid the server will add the plan to memory, 
create a list of users for that plan and create a code for the
plan. This information will be then sent back to the user.

If the plan is invalid it will return an error
"""
@server.route('/addplan', methods=['POST'])
def add_plan():

    apikey = request.args.get('apikey')
    user_nick = request.args.get('nick')
    user_lon = request.args.get('lon')
    user_lat = request.args.get('lat')

    if request.method == 'POST' and apikey == APIKEY and\
        request.get_json() and 'name' in request.get_json():

        newPlan = plan(request.get_json())

        if newPlan.name != "INVALID PLAN":
            code = cm.createCodeForPlan(plans)

            users[code] = {user_nick : user(user_nick,user_lon,user_lat)}
            plans[code] = newPlan

            return barJsons.createAddPlanJson(code,plans[code],users[code])

        else:
            #Bad Plan
            return make_response(jsonify({'error': 'Invalid Plan'}), 200)
    else:
        #Bad Key
        return make_response(jsonify({'error': 'Bad API key'}), 200)


"""
barcrawlrserver/getplan(code,apikey)

This target allows other clients to connect to a plan that
exists on the server

If the plan exists on the server the client will be sent the
list of users and the plan the code is attached to. The client
also has to send their information

If it fails the client will be returned an error
"""
@server.route('/getplan', methods=['GET'])
def get_plan():

    #url parameters
    apikey = request.args.get('apikey')
    plan_id = request.args.get('code')
    user_nick = request.args.get('nick')
    user_lon = request.args.get('lon')
    user_lat = request.args.get('lat')

    if apikey == APIKEY and plan_id in plans.keys() \
        and user_nick != "" and user_nick not in users[plan_id].keys():

        users[plan_id][user_nick] = user(user_nick,user_lon,user_lat)
        return barJsons.createGetPlanJson(plans[plan_id],users[plan_id])

    else:
        #Errors
        #Bad plan id
        if apikey == APIKEY:
            if plan_id not in plans.keys():
                return make_response(jsonify({'error': 'Plan doesn\'t exist'}), 200)
            #bad user id
            else:
                return make_response(jsonify({'error': 'Username already exists'}), 200)
        #Bad API key
        else:
            return make_response(jsonify({'error': 'Bad API key'}), 200)

    #something went horribly wrong
    abort(400)


"""
barcrawlrserver/update(code,nick,apikey,lon,lat)

This target allows clients to send and recieve user
information

The user sends the code of their plan and their
information through url parameters. They get sent
the list of current user information if the plan exists
"""
@server.route('/update', methods=['GET'])
def update_info():

    #url parameters
    apikey = request.args.get('apikey')
    plan_id = request.args.get('code')
    user_nick = request.args.get('nick')
    user_lon = request.args.get('lon')
    user_lat = request.args.get('lat')

    if apikey == APIKEY and plan_id in plans.keys()\
        and user_nick in users[plan_id].keys():

        users[plan_id][user_nick].lon = float(user_lon)
        users[plan_id][user_nick].lat = float(user_lat)
        
        return barJsons.createUsersJsonFromDict(users[plan_id])
    else:
        #Errors
        #Bad plan id
        if apikey == APIKEY:
            if plan_id not in plans.keys():
                return make_response(jsonify({'error': 'Plan doesn\'t exist'}), 200)
            #bad user_id
            else:
                return make_response(jsonify({'error': 'Username doesn\'t exist'}), 200)

        #Bad API key
        else:
            return make_response(jsonify({'error': 'Bad API key'}), 200)

    #something went horribly wrong
    abort(400)


"""
barcrawlrserver/disconnect(code,nick,apikey)

This target lets the client disconnect from the list
of active users associated with the plan

If there are no users left connected the plan will be deleted
"""
@server.route('/disconnect', methods=['GET'])
def user_disconnect():

    #url parameters
    apikey = request.args.get('apikey')
    plan_id = request.args.get('code')
    user_nick = request.args.get('nick')

    if apikey == APIKEY and plan_id in plans.keys()\
        and user_nick in users[plan_id].keys():

        del users[plan_id][user_nick]

        if len(users[plan_id]) == 0:
            del plans[plan_id]
            del users[plan_id]

            return make_response(jsonify({'status': 'Success, user removed, plan deleted'}), 200)

        return make_response(jsonify({'status': 'Success, user removed'}), 200)
    else:
        #Errors
        #Bad plan id
        if apikey == APIKEY:
            if plan_id not in plans.keys():
                return make_response(jsonify({'error': 'Plan doesn\'t exist'}), 200)
            #bad user_id
            else:
                return make_response(jsonify({'error': 'Username doesn\'t exist'}), 200)

        #Bad API key
        else:
            return make_response(jsonify({'error': 'Bad API key'}), 200)

    #something went horribly wrong
    abort(400)

#Index, returns a message about how there's no point in going there
@server.route('/')
def index():
    return INDEX_MESSAGE

# 404 Error Handler
@server.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
