"""
Customer class
"""
from marshmallow import Schema, fields, validates, ValidationError
from .customer_type import CustomerType


class Customer:

    def __init__(self, cust_id, name, address, cust_type):
        self.id = cust_id
        self.name = name
        self.address = address
        self.type = cust_type
        self.is_premium = (cust_type == CustomerType.PREMIUM)


"""
CustomerSchema class
"""


class CustomerSchema(Schema):
    id = fields.Integer()
    name = fields.Str(required=True)
    address = fields.Str(required=True)
    type = fields.Str()
    is_premium = fields.Boolean()

    @validates("name")
    def validate_name(self, value):
        if not value or len(value) < 1:
            raise ValidationError("Invalid name value")