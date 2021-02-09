"""
Bluehost Customer product order tracker service
"""

from flask import Flask, request
from .model.customer_manager import CustomerManager
from .model.product_manager import ProductManager
from .model.order_manager import OrderManager

# Create the service app
app = Flask(__name__)

"""
customers endpoints
"""
customer_mgr = CustomerManager.get_instance()

@app.route('/customers')
def get_customers():
    return customer_mgr.get_all()

@app.route('/customers/<customer_id>')
def get_customer(customer_id):
    return customer_mgr.get(customer_id)

@app.route('/customers', methods=['POST'])
def add_customer():
    return customer_mgr.add(request)

@app.route('/customers/<customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    return customer_mgr.delete(customer_id)


"""
products endpoints
"""
product_mgr = ProductManager.get_instance()

@app.route('/products')
def get_products():
    return product_mgr.get_all()

@app.route('/products/<product_id>')
def get_product(product_id):
    return product_mgr.get(product_id)

@app.route('/products', methods=['POST'])
def add_product():
    return product_mgr.add(request)

@app.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    return product_mgr.delete(product_id)


"""
orders endpoints
"""
order_mgr = OrderManager.get_instance()

@app.route('/orders')
def get_orders():
    return order_mgr.get_all()

@app.route('/orders/<order_id>')
def get_order(order_id):
    return order_mgr.get(order_id)

@app.route('/orders', methods=['POST'])
def add_order():
    return order_mgr.add(request)

@app.route('/orders/<order_id>/items', methods=['POST'])
def add_order_item(order_id):
    return order_mgr.add_order_item(order_id, request)

@app.route('/orders/<order_id>/place', methods=['POST'])
def place_order(order_id):
    return order_mgr.place_order(order_id)

@app.route('/orders/<order_id>', methods=['DELETE'])
def delete_order(order_id):
    return order_mgr.delete(order_id)



"""
 Main section
"""
if __name__ == "__main__":
    app.run()
