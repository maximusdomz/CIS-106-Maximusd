class Employee:
    # Employee with a first name, last name, annual salary, and a 10% bonus of their salary.
    def __init__(self, employee_first_name, employee_last_name, annual_salary):
        self.employee_first_name = employee_first_name
        self.employee_last_name = employee_last_name
        self.annual_salary = annual_salary

    def get_employee_full_name(self):
        return f"{self.employee_first_name} {self.employee_last_name}"

    def calculate_bonus(self):
        # Calculates the employee's bonus at 10%.
        return self.annual_salary * 0.10

class Manager(Employee):
    # Overrides the bonus calculation to 20% and adds a long-term bonus for the Manager.
    def __init__(self, employee_first_name, employee_last_name, annual_salary):
        super().__init__(employee_first_name, employee_last_name, annual_salary)

    def calculate_bonus(self):
        # Overrides the bonus calculation for managers at 20%.
        return self.annual_salary * 0.20

    def calculate_long_term_bonus(self):
        # Calculates the manager's long-term bonus at 50%.
        return self.annual_salary * 0.50

# Display Results.
if __name__ == "__main__":
    # Test Employee class.
    employee1 = Employee("Maximus", "Dominguez", 60000)
    print(f"Employee: {employee1.get_employee_full_name()}")
    print(f"Annual Salary: ${employee1.annual_salary:,.2f}")
    print(f"Employee Bonus: ${employee1.calculate_bonus():,.2f}\n")

    # Test Manager class.
    manager1 = Manager("Marcus", "Dominick", 100000)
    print(f"Manager: {manager1.get_employee_full_name()}")
    print(f"Annual Salary: ${manager1.annual_salary:,.2f}")
    print(f"Manager Bonus: ${manager1.calculate_bonus():,.2f}")
    print(f"Manager Long-Term Bonus: ${manager1.calculate_long_term_bonus():,.2f}")