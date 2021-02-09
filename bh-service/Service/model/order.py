from marshmallow import Schema, fields
from .order_specs import OrderStatus

"""
OrderItem class
"""


class OrderItem:

    def __init__(self, product_id, quantity, price):
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
        self.total_cost = self.quantity * self.price

    def update_quantity(self, quantity):
        self.quantity += quantity
        self.total_cost = self.quantity * self.price


"""
OrderItemSchema class
"""


class OrderItemSchema(Schema):
    product_id = fields.Integer()
    quantity = fields.Integer()
    price = fields.Decimal()
    total_cost = fields.Decimal()


"""
Order class
"""


class Order:

    def __init__(self, order_id, customer_id, is_premium):
        self.id = order_id
        self.customer_id = customer_id
        self.is_premium = is_premium
        self.items = []
        self.shipping = 0.00
        if not self.is_premium:
            self.shipping = 5.11
        self.order_cost = 0.00
        self.order_status = OrderStatus.IN_CART

    def add_item(self, new_item):
        for item in self.items:
            if item.product_id == new_item.product_id:
                item.update_quantity(new_item.quantity)
                return
        self.items.append(new_item)
        self._compute_totals()

    def _compute_totals(self):
        self.order_cost = self.shipping
        for item in self.items:
            self.order_cost += item.total_cost

    def place_order(self):
        self.order_status = OrderStatus.PLACED


"""
OrderSchema class
"""


class OrderSchema(Schema):
    id = fields.Integer()
    customer_id = fields.Integer()
    is_premium = fields.Boolean()
    items = fields.Nested(OrderItemSchema, many=True)
    shipping = fields.Decimal()
    order_cost = fields.Decimal()
    order_status = fields.Str()
