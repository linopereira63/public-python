"""
Product and ProductSchema classes
"""
from marshmallow import Schema, fields


class Product:

    def __init__(self, prod_id, name, description, category, price, stock_count, size=None, color=None):
        self.id = prod_id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.stock_count = stock_count
        self.size = size
        self.color = color


class ProductSchema(Schema):
    id = fields.Integer()
    name = fields.Str()
    description = fields.Str()
    price = fields.Decimal()
    category = fields.Str()
    stock_count = fields.Integer()
    size = fields.Str()
    color = fields.Str()
