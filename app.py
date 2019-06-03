from flask import Flask
from marshmallow import Schema, fields, INCLUDE, pprint, ValidationError
from flask import abort, request, jsonify
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

if __name__ == '__main__':
    app.run()
