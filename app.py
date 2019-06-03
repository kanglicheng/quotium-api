import json
from flask import Flask
from marshmallow import Schema, fields, INCLUDE, pprint, ValidationError
from flask import abort, request, jsonify
from calculate_estimates import RentalEstimate

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Hello World!'

@app.route('/test', methods=['POST'])
def post_test():
    if not request.json:
        abort(400)
    else:
        return jsonify(request.json)

@app.route('/submit', methods=['POST'])
def validate_post_data():
    if not request.json:
        abort(400)
    try:
        # pprint(request.json)
        # return request.json
        a = property_schema.load(request.json)
        estimate = process_property_data(a)
        a['estimate'] = estimate
        return jsonify(a)
        #return jsonify(request.json), 201
    except ValidationError as error:
        return jsonify(error.messages), 422

if __name__ == '__main__':
    app.run()
