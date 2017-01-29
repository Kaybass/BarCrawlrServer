from flask import Flask, jsonify, current_app

from BarCrawlrServer.model.plan import plan

server = Flask(__name__)

plans = [
    plan('{"Name":"test_plan_1","Address":"Oceanic location","Location":[0,0],"Note":"Test plan for testing"}')
]

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
@server.route('/plan', methods=['GET'])
def get_all_plans():
    return jsonify({'plan 1': plans['plan'].jsonify()})


if __name__ == '__main__':
    server.run(debug=True)
