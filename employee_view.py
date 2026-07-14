from data import data
def view_employees():
    if not employees:
        print("\nNo employees found\n")
        return
    print("\nEmployee list")
    for emp in employees:
        print(f"id: {emp['id']}")
        print(f"name: {emp['Name']}")
        print(f"salary: {emp['salary']}")