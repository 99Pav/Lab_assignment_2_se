class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"

class EmployeeTable:
    def __init__(self, employees):
        self.employees = employees

    def print_table(self):
        for employee in self.employees:
            print(employee)

    def sort_table(self, key):
        self.employees.sort(key=lambda x: getattr(x, key.lower()))

if __name__ == "__main__":
    employees_data = [
        Employee("161E90", "Ramu", 35, 59000),
        Employee("171E22", "Tejas", 30, 82100),
        Employee("171G55", "Abhi", 25, 100000),
        Employee("152K46", "Jaya", 32, 85000)
    ]

    employee_table = EmployeeTable(employees_data)

    print("Original Employee Table:")
    employee_table.print_table()

    sorting_options = {
        1: "age",
        2: "name",
        3: "salary"
    }

    sort_option = int(input("Choose sorting parameter (1. Age, 2. Name, 3. Salary): "))
    
    if sort_option in sorting_options:
        key_to_sort = sorting_options[sort_option]
        employee_table.sort_table(key_to_sort)

        print(f"\nEmployee Table sorted by {key_to_sort}:")
        employee_table.print_table()
    else:
        print("Invalid sorting option. Please choose a valid option.")
