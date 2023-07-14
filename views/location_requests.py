LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    }
]

def get_single_location(id):
    "function returns one dictionary"
    requested_location = None

    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location

    return requested_location

def get_all_locations():
    "function returns list"
    return LOCATIONS

def create_location(location):
    "docstring"
    last_location = LOCATIONS[-1]["id"]

    new_location = last_location + 1
    
    location["id"] = new_location

    LOCATIONS.append(location)

    return location

def delete_location(id):
    '''function to delete'''
    location_index = -1
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            location_index = index
    if location_index >= 0:
        LOCATIONS.pop(location_index)

def update_location(id, new_location):
    '''function to update location'''
    for index, location in enumerate(LOCATIONS):
        if location['id'] == id:
            LOCATIONS[index] = new_location
            break 


