#### **Bluehost Customer product order tracker service**
##### Background
The mail-order anvil business is slowing, and the Acme company has decided to join the modern world.
They’ve created a new Acme Web subsidiary, and it needs a web service for tracking customer products.
You have been hired to create a prototype for them to evaluate.

##### Prototype
The full prototype will support CRUD operations for customers, products, and orders. Each operation
validates its input before executing the requested action.

The company has two customer types (standard and premium). Premium customers do not pay shipping
and are eligible for a free order of Acme Aspirin once per month. Customer data is limited to name and
address.

The web service will initially support four basic products: anvils, super costumes, rocket-powered roller
skates, and aspirin. Basic product data is limited to name, price, description, and the number in stock.
Both the costumes and the roller skates are available in different sizes and colors, so they also need
these two pieces of data.

Order data is limited to the customer Id, the product Id, the quantity ordered, the shipping charge, and the
total price.

##### Deliverable
The single deliverable is the link to a GitHub repo containing both your code for the exercise and a
README file listing a) any assumptions you’ve made in designing your solution, and b) optionally, a list of
additional work you would have done had time permitted.

#### My Assumptions:

##### Customer Use Case:

Add customer, including authentication/authorization, assumed to have happened beforehand.

Customer authenticates, then gets customer via ID.

Query for available products (currently getting all).

Create Order with customer_id and is_premium.

Add item to order with product_id, quantity and price.

Remove item from order (not implemented here).

Place Order, after which, the order cannot be changed.

View order by customer_id (currently getting all).


##### Admin/Backend Use Cases Considered:

Get all customers.

Get products running low in stock and refilling products.

Get PLACED Orders and fulfill them.


##### Other assumptions:
Order.status dictates the state of the order, which is fine here. For scalability, orders would get moved from IN_CART 
queue to PLACED queue and so on.


#### Additional work required: 

Add unit tests for all.

Add validation for all fields.

Add Edit methods, which would be done via a PUT and return NO_CONTENT on success.

Restrict some fields from being exposed, such as Customer.type.

Add get_available_products()

Add remove_order_item(product_id)

Add update_order_item(request), uses product_id to find item to be updated

Add cancel_order() but only if Order.status = PLACED

Add get_orders_by_customer_id(customer_id)




