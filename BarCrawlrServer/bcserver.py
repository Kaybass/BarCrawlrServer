from flask import Flask, jsonify, current_app, abort, make_response

from BarCrawlrServer.model.plan import plan

server = Flask(__name__)

plans = [
    {
        'id': 0,
        'plan': plan('{"Name":"test_plan_1","Address":"Oceanic location","Location":[0,0],"Note":"Test plan for testing"}')
    }
]

@server.route('/')
def index():
    return "Welcome to Bar Crawlr Server"

@server.route('/plan', methods=['POST'])
def create_plan():
    if not "Name" in request.json:
        abort(400)
    plans.append(plan(request.json))
    return len(plans)
    
@server.route('/plans', methods=['GET'])
def get_all_plans():
    return jsonify({'plan 1': plans['plan'].jsonify()})

@server.route('/plan/<int:plan_id>',methods=['GET'])
def get_plan(plan_id):
    p = [plan for plan in plans if plan['id'] == plan_id]
    if len(p) == 0:
        abort(400)
    return p[plan_id].plan.jsonify()

@server.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    server.run(debug=True)