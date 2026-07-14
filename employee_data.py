from data import data
def add_employee():
    emp_id = input("Enter employee id: ")
    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))
    employee = { "id": emp_id, "name": name, "salary": salary }
    employees.append(employee)
    print("\nEmployee added successfully\n")