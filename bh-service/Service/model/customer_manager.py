"""
CustomerManager singleton class - manages all customer actions and keeps the customer DB in memory.
"""
from flask import jsonify
from http import HTTPStatus

from .customer import Customer, CustomerSchema
from .customer_type import CustomerType
from .base_manager import BaseManager


class CustomerManager(BaseManager):
    # Singleton instance that everyone should call
    @staticmethod
    def get_instance():
        if not BaseManager._instance:
            BaseManager._instance = CustomerManager()
        return BaseManager._instance

    def __init__(self):
        # K:id, V:customer
        self._customers = {}
        self._create_initial_data()

    def _create_initial_data(self):
        cid = self._get_next_id()
        self._customers[cid] = Customer(cid, "Joe", "123 Here St, Boulder, CO", CustomerType.STANDARD)
        cid = self._get_next_id()
        self._customers[cid] = Customer(cid, "Betty", "456 There St, Boulder, CO", CustomerType.PREMIUM)

    def get_all(self):
        # TODO:  cache this
        temp_list = [c for c in self._customers.values()]
        schema = CustomerSchema(many=True)
        return jsonify(schema.dump(temp_list).data)

    def get(self, customer_id):
        # TODO: add checking for non-int customer_id
        cid = int(customer_id)
        if cid in self._customers:
            cust = self._customers[cid]
            schema = CustomerSchema()
            return jsonify(schema.dump(cust).data)
        else:
            return "customer ID " + customer_id + " - Not Found", HTTPStatus.NOT_FOUND

    def add(self, request):
        customer = CustomerSchema().load(request.get_json())
        cid = self._get_next_id()
        customer.data["id"] = cid
        self._customers[cid] = customer.data
        return "Added customer ID " + str(cid), HTTPStatus.CREATED

    def delete(self, customer_id):
        # TODO: add checking for non-int customer_id
        cid = int(customer_id)
        if cid in self._customers:
            self._customers.pop(cid)
            return "Deleted customer ID " + str(cid), HTTPStatus.NO_CONTENT
        else:
            return "customer ID " + customer_id + " - Not Found", HTTPStatus.NOT_FOUND


