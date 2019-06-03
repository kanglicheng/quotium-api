import flask
import json
from flask import Flask, abort, request, jsonify
#from data_validation import PropertySubmissionSchema
from marshmallow import Schema, fields, INCLUDE, pprint, ValidationError
#from calculate_estimates import RentalEstimate

APP = Flask(__name__)

@APP.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    APP.run()
