"""
CustomerType class - used by Customer class
"""
from enum import Enum


class CustomerType(Enum):
    STANDARD = "STANDARD"
    PREMIUM = "PREMIUM"
