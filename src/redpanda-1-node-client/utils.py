import os
import json

def load_data():
    db_path = os.path.join('db', 'data.json')
    with open(db_path, 'r') as file:
        orders = json.load(file)
    return orders