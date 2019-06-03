import json
from marshmallow import Schema, fields, INCLUDE, pprint, ValidationError

class PropertySubmissionSchema(Schema):
    email = fields.Str(required=True)
    property_address = fields.Str(required=True)
    zip_code = fields.Int(required=True)
    number_bedrooms = fields.Int(required=True)
    number_bathrooms = fields.Int(required=True)
    square_footage = fields.Int(required=True)

    class Meta:
        unkcnown = INCLUDE
