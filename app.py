from flask import Flask
from marshmallow import Schema, fields, INCLUDE, pprint, ValidationError
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
