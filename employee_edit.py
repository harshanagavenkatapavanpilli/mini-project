from data import data
def edit_employee():
    emp_id = input("Enter employee id to edit: ")
    for emp in employees:
        if emp["id"] == emp_id:
            emp["name"] = input("Enter new name: ")
            emp["salary"] = float(input("Enter new salary: "))
            print("\nEmployee updated\n")
            return
    print("\n not found\n")