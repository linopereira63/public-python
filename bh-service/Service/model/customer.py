"""
Customer class
"""
from marshmallow import Schema, fields
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
    name = fields.Str()
    address = fields.Str()
    type = fields.Str()
    is_premium = fields.Boolean()
