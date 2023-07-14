EMPLOYEES = [
    {
        "id": 1,
        "name": "Jenna Solis"
    }
]

def get_all_employees():
    "function to return all employees"
    return EMPLOYEES

def get_single_employee(id):
    "function to return single dictionary"
    requested_employee = None
    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    '''function adds employee to list'''
    last_employee = EMPLOYEES[-1]["id"]

    new_employee = last_employee +1

    employee["id"] = new_employee

    EMPLOYEES.append(employee)

    return employee

def delete_employee(id):
    '''function ot remove employee'''
    employee_index = -1
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index
        
        if employee_index >= 0:
            EMPLOYEES.pop(employee_index)

def update_employee(id, new_employee):
    '''function to update employee'''
    for index, employee in enumerate(EMPLOYEES):
        if employee['id'] == id:
            EMPLOYEES[index] = new_employee
            break 