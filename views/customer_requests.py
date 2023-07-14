CUSTOMERS = [
    {
        "id": 1,
        "name": "Ryan Tanya"
    }
]

def get_single_customer(id):
    "function returns one dictionary"
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

def get_all_customers():
    "function returns list"
    return CUSTOMERS

def create_customer(customer):
    '''function adds customer dict to list'''
    last_customer = CUSTOMERS[-1]["id"]

    new_customer = last_customer + 1

    customer["id"] = new_customer

    CUSTOMERS.append(customer)

    return customer

def delete_customer(id):
    '''function to delete'''
    customer_index = -1
    for index, customer in enumerate(CUSTOMERS):
        if customer['id'] == id:
            customer_index = index
    
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    '''function to update customer'''
    for index, customer in enumerate(CUSTOMERS):
        if customer['id'] == id:
            CUSTOMERS[index] = new_customer
            break 

