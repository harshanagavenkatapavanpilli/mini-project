from employee_data import employee_data
from employee_delete import employee_delete
from employee_search import employee_search
from employee_edit import employee_edit
from employee_view import employee_view

while True:
    print("\n Employee management system ")
    print("1. Add employee")
    print("2. View employees")
    print("3. Search employee")
    print("4. Edit employee")
    print("5. Delete employee")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        employee_data()
    elif choice == "2":
        employee_view()
    elif choice == "3":
        employee_search()
    elif choice == "4":
        employee_edit()
    elif choice == "5":
        employee_delete()
    elif choice == "6":
        print("thank")
        break
    else:
        print("Invalid")