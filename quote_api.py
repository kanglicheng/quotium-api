import flask
import json
from flask import abort, request, jsonify
from data_validation import PropertySubmissionSchema
from marshmallow import Schema, fields, INCLUDE, pprint, ValidationError
from calculate_estimates import RentalEstimate

app = flask.Flask(__name__)
app.config["DEBUG"] = True

property_schema = PropertySubmissionSchema()

@app.route('/', methods=['GET'])
def home():
    return "This is a test"

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

    #request_json = request.json
    #print(request_json['email'])



app.run()

#curl -i -H "Content-Type: application/json" -X POST -d '{"email":"read", "property_address":"5 my property address", "zip_code":14853,
 #"number_bedrooms":5, "number_bathrooms":5, "square_footage":10000}' http://127.0.0.1:5000/submit
#curl -i -H "Content-Type: application/json" -X POST -d '{"email":"read", "number_bedrooms":5}' http://127.0.0.1:5000/submit
