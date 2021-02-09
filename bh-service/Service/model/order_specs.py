"""
Order spec classes - used by Order class
"""
from enum import Enum


class OrderStatus(Enum):
    IN_CART = "IN_CART"
    PLACED = "PLACED"
    IN_TRANSIT = "IN_TRANSIT"
    DELIVERED = "DELIVERED"

