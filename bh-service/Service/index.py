"""
Bluehost Customer product order tracker service
"""

from flask import Flask, Response, jsonify, request
from .model.customer_manager import CustomerManager

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
 Main section
"""
if __name__ == "__main__":
    app.run()
