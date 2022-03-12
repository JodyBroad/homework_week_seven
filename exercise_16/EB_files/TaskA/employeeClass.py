from personClass import Person

class Employee(Person):
    company_name = "CompanyA"
    count = 0

    def __init__(self, name, age, location, department, salary, payroll_number):
        super().__init__(name, age, location)
        Employee.count = Employee.count + 1
        self.department = department
        self.salary = salary
        self.payroll_number = payroll_number

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

    def get_department(self):
        return self.department

    def set_department(self, salary):
        self.department = department

    @classmethod
    def change_company(cls, company_name):
        cls.company_name = company_name

    def work(self):
        print(f'{self.name} works in {self.department} at {self.company_name}. Their salary is £{self.salary}')

james = Employee("James", 23, "London", "Finance", 33000, 5367789)
sarah = Employee("Sarah", 29, "Manchester", "Marketing", 55000, 54345567)

print(f'The total number of employees at {Employee.company_name} is {Employee.count}')

james.work()
sarah.work()