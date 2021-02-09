"""
Bluehost Customer product order tracker service
"""

from flask import Flask, request
from .model.customer_manager import CustomerManager
from .model.product_manager import ProductManager

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
 Main section
"""
if __name__ == "__main__":
    app.run()
