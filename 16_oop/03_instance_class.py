class Employee:
    company = "Asus"

    def __init__(self, salary, name, bond, company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(
            f"The name of the employee is {self.name}. Salary is {self.salary} bond {self.bond}"
        )


e1 = Employee(3000, "dat", 4, "Tesla")

print(Employee.company)

e1.get_info()
