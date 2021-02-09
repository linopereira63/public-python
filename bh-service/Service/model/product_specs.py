"""
ProductCategory class - used by Product class
"""
from enum import Enum


class ProductCategory(Enum):
    TOOLS = "TOOLS"
    SEASONAL = "SEASONAL"
    FOOTWEAR = "FOOTWEAR"
    DRUGS = "DRUGS"


class ProductSize(Enum):
    SMALL = "SMALL"
    MEDIUM = "MEDIUM"
    LARGE = "LARGE"


class ProductColor(Enum):
    RED = "RED"
    BLUE = "BLUE"
    PURPLE = "PURPLE"
