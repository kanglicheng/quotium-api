import json
from flask import Flask
from marshmallow import Schema, fields, INCLUDE, pprint, ValidationError
from data_validation import PropertySubmissionSchema
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

property_schema = PropertySubmissionSchema()

def process_property_data(data):
    rt = RentalEstimate()
    airbnb_tot, full_home_tot = rt.yearly_airbnb_total(), rt.yearly_full_home()
    renter_tot = rt.yearly_renter_rent()
    if airbnb_tot + renter_tot > 4000 + full_home_tot:
        return int((1.1*airbnb_tot + full_home_tot)/12)
    else:
        return "N/A"

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
