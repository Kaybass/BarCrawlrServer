from flask import Flask, jsonify, current_app

from BarCrawlrServer.model.plan import plan

server = Flask(__name__)

plans = [
    plan('{"Name":"test_plan_1","Address":"Oceanic location","Location":[0,0],"Note":"Test plan for testing"}')
]

@server.route('/')
def index():
    return "Welcome to Bar Crawlr Server"

@server.route('/plan', methods=['POST'])
def create_plan():
    if not request.json or not 'name' in request.json:
        abort(400)
    plans.append(plan(request.json))
    return len(plans)
    
@server.route('/plan', methods=['GET'])
def get_all_plans():
    return jsonify({'plan 1': plans['plan'].jsonify()})
#def get_plan(plan_id):
#    p = [plan for plan in plans if plans['id'] == plan_id]
#    if len(plans) == 0:
#        abort(400)
#    if len(plan) == 0:
#        abort(400)
#    return plans[plan_id].jsonify()

if __name__ == '__main__':
    server.run(debug=True)
