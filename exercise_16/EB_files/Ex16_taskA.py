class Person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def show(self):
        print(f"{self.name} is {self.age} and lives in {self.location}")

class Employee(Person):
    company_name = "CompanyA"
    count = 0

    def __init__(self, name, age, location, department, salary):
        super().__init__(name, age, location)
        Employee.count = Employee.count + 1
        self.department = department
        self.salary = salary

    def work(self):
        print(f'{self.name} works in {self.department} at {self.company_name}. Their salary is £{self.salary}')

class Customer(Person):
    company_name = "CompanyB"
    count = 0

    def __init__(self, name, age, location, spend_amount, number_items_bought):
        super().__init__(name, age, location)
        Customer.count = Customer.count + 1
        self.spend_amount = spend_amount
        self.number_items_bought = number_items_bought

    def shopping(self):
        print(f'{self.name} has spent £{self.spend_amount} at {self.company_name}. They bought {self.number_items_bought} items')



james = Employee("James", 23, "London", "Finance", 33000)
sarah = Employee("Sarah", 29, "Manchester", "Marketing", 55000)
jasmine = Customer("Jasmine", 35, "Sheffield", 53, 4)
print(f'The total number of employees at {Employee.company_name} is {Employee.count}')
james.work()
sarah.work()
print(f'{Customer.company_name} has had {Customer.count} customers')
jasmine.show()
jasmine.shopping()
jasmine.set_age(36)
jasmine.show()



