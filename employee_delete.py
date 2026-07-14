from data import data
def delete_employee():
    emp_id = input("Enter employee id to delete: ")
    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            print("\n Deleted successfully\n")
            return
    print("\nEmployee not found\n")