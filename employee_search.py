from data import data
def search_employee():
    emp_id = input("Enter employee id to search: ")
    for emp in employees:
        if emp["id"] == emp_id:
            print("\nEmployee found")
            print(f"id: {emp['id']}")
            print(f"name: {emp['name']}")
            print(f"salary: {emp['salary']}\n")
            return
    print("\nEmployee not found\n")