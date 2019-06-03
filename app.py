import flask
import json
from flask import abort, request, jsonify
from data_validation import PropertySubmissionSchema
from marshmallow import Schema, fields, INCLUDE, pprint, ValidationError
from calculate_estimates import RentalEstimate

app = flask.Flask(__name__)

# property_schema = PropertySubmissionSchema()

@app.route('/', methods=['GET'])
def home():
    return "This is a test"

if __name__ == '__main__':
    app.run()
