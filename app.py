import flask
import json
from flask import abort, request, jsonify
from data_validation import PropertySubmissionSchema
from marshmallow import Schema, fields, INCLUDE, pprint, ValidationError
from calculate_estimates import RentalEstimate

app = flask.Flask(__name__)
app.config["DEBUG"] = True

property_schema = PropertySubmissionSchema()

#@app.route('/', methods=['GET'])
@app.route('/')
def home():
    return "This is a test"

if __name__ == '__main__':
    app.run()
