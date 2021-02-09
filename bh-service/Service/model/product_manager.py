"""
ProductManager singleton class - manages all product actions and keeps the product DB in memory.
"""
from flask import jsonify
from http import HTTPStatus

from .product import Product, ProductSchema
from .product_specs import ProductCategory, ProductSize, ProductColor
from .base_manager import BaseManager


class ProductManager(BaseManager):
    # Singleton instance that everyone should call
    _instance = None

    @staticmethod
    def get_instance():
        if not ProductManager._instance:
            ProductManager._instance = ProductManager()
        return ProductManager._instance

    def __init__(self):
        super().__init__()
        # K:id, V:product
        self._products = {}
        self._create_initial_data()

    # TODO: remove this dummy data
    def _create_initial_data(self):
        pid = self._get_next_id()
        self._products[pid] = Product(pid, "Bronze Anvil", "A fine Bronze Anvil", ProductCategory.TOOLS, 69.99, 20)
        pid = self._get_next_id()
        self._products[pid] = Product(pid, "Batman Costume", "A fine Batman Costume", ProductCategory.SEASONAL, 22.99, 52, ProductSize.SMALL, ProductColor.BLUE)
        pid = self._get_next_id()
        self._products[pid] = Product(pid, "Superman Costume", "A fine Superman Costume", ProductCategory.SEASONAL, 25.99, 65, ProductSize.LARGE, ProductColor.RED)
        pid = self._get_next_id()
        self._products[pid] = Product(pid, "Rocket-Powered Roller Skates", "A fast pair of Rocket-Powered Roller Skates", ProductCategory.SEASONAL, 163.99, 12, ProductSize.MEDIUM, ProductColor.PURPLE)
        pid = self._get_next_id()
        self._products[pid] = Product(pid, "Acme Aspirin", "Generic Acme Aspirin", ProductCategory.DRUGS, 5.99, 125)

    def get_all(self):
        # TODO:  cache this
        temp_list = [c for c in self._products.values()]
        schema = ProductSchema(many=True)
        return jsonify(schema.dump(temp_list).data)

    def get(self, product_id):
        pid, err = BaseManager.convert_string_id(product_id)
        if err:
            return err, HTTPStatus.BAD_REQUEST
        if pid in self._products:
            prod = self._products[pid]
            schema = ProductSchema()
            return jsonify(schema.dump(prod).data)
        else:
            return "product ID " + product_id + " - Not Found", HTTPStatus.NOT_FOUND

    def add(self, request):
        product = ProductSchema().load(request.get_json())
        pid = self._get_next_id()
        product.data["id"] = pid
        self._products[pid] = product.data
        return "Added product ID " + str(pid), HTTPStatus.CREATED

    def delete(self, product_id):
        pid, err = BaseManager.convert_string_id(product_id)
        if err:
            return err, HTTPStatus.BAD_REQUEST
        if pid in self._products:
            self._products.pop(pid)
            return "Deleted product ID " + str(pid), HTTPStatus.NO_CONTENT
        else:
            return "product ID " + product_id + " - Not Found", HTTPStatus.NOT_FOUND


