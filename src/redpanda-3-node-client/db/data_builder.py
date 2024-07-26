import json
from datetime import datetime
import random

orders_data = []  # Empty list to store order data

for i in range(100):
    order_id = f"{10000 + i}"  # Generates order IDs starting from 10000
    product_id = f"A{200 + i}"  # Generates product IDs starting from A200
    quantity = random.randint(1, 10)  # Random quantity between 1 and 10
    status = "received"  # Status is always "received"
    timestamp = datetime.now().isoformat()  # Current timestamp for each order
    
    # Append the new order to the orders_data list
    orders_data.append({
        "order_id": order_id,
        "product_id": product_id,
        "quantity": quantity,
        "status": status,
        "timestamp": timestamp
    })

# Write the orders_data list to data.json
with open('data.json', 'w') as f:
    json.dump(orders_data, f, indent=4)
