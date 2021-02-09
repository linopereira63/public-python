"""
OrderManager singleton class - manages all order actions and keeps the orders DB in memory.
"""
from flask import jsonify
from http import HTTPStatus

from .order import Order, OrderSchema, OrderItem, OrderItemSchema
from .order_specs import OrderStatus
from .base_manager import BaseManager


class OrderManager(BaseManager):
    # Singleton instance that everyone should call
    _instance = None

    @staticmethod
    def get_instance():
        if not OrderManager._instance:
            OrderManager._instance = OrderManager()
        return OrderManager._instance

    def __init__(self):
        super().__init__()
        # K:id, V:order
        self._orders = {}

    def get_all(self):
        temp_list = [c for c in self._orders.values()]
        schema = OrderSchema(many=True)
        return jsonify(schema.dump(temp_list).data)

    def _get_order(self, order_id):
        oid, err = BaseManager.convert_string_id(order_id)
        if err:
            return None, err, HTTPStatus.BAD_REQUEST
        if oid in self._orders:
            order = self._orders[oid]
            return order, err, None
        else:
            return None, "order ID " + order_id + " - Not Found", HTTPStatus.NOT_FOUND

    def get(self, order_id):
        order, err, status = self._get_order(order_id)
        if err:
            return err, status
        schema = OrderSchema()
        return jsonify(schema.dump(order).data)

    def add(self, request):
        order = OrderSchema().load(request.get_json())
        oid = self._get_next_id()
        self._orders[oid] = Order(oid, order.data["customer_id"], order.data["is_premium"])
        return "Added order ID " + str(oid), HTTPStatus.CREATED

    def add_order_item(self, order_id, request):
        order, err, status = self._get_order(order_id)
        if err:
            return err, status
        if order.order_status != OrderStatus.IN_CART:
            return "Order ID " + order_id +" can no longer be modified", HTTPStatus.FORBIDDEN
        if not request or not request.get_json():
            return "Invalid Request", HTTPStatus.BAD_REQUEST

        item = OrderItemSchema().load(request.get_json())
        order.add_item(OrderItem(item.data["product_id"], item.data["quantity"], item.data["price"]))
        return "Added item to order ID " + order_id, HTTPStatus.CREATED

    def place_order(self, order_id):
        oid, err = BaseManager.convert_string_id(order_id)
        if err:
            return err, HTTPStatus.BAD_REQUEST
        if oid in self._orders:
            order = self._orders[oid]
            if order.order_status != OrderStatus.IN_CART:
                return "Order ID " + order_id + " has already been placed", HTTPStatus.NO_CONTENT
            order.place_order()
            return "Placed order ID " + str(oid), HTTPStatus.NO_CONTENT
        else:
            return "order ID " + order_id + " - Not Found", HTTPStatus.NOT_FOUND

    def delete(self, order_id):
        oid, err = BaseManager.convert_string_id(order_id)
        if err:
            return err, HTTPStatus.BAD_REQUEST
        if oid in self._orders:
            self._orders.pop(oid)
            return "Deleted order ID " + str(oid), HTTPStatus.NO_CONTENT
        else:
            return "order ID " + order_id + " - Not Found", HTTPStatus.NOT_FOUND


