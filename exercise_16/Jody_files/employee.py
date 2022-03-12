# employee is subclass of person, so need to import
from person import Person


class Employee(Person):
    num_of_employees = 0

    # annual payrise as a class variable to allow you to update for all employees simultaneously
    annual_payrise = 1.05

    def __init__(self, first_name, surname, job_title, department, salary):
        super().__init__(first_name, surname)
        self.__job_title = job_title
        self.__department = department
        self.__salary = salary
        Employee.num_of_employees += 1

    def apply_payrise(self):
        self.__salary = int(self.__salary * self.annual_payrise)

    # getter - job title
    def get_job_title(self):
        return self.__job_title

    # setter - job title
    def set_job_title(self, job_title):
        self.__job_title = job_title

    # getter - department
    def get_department(self):
        return self.__department

    # setter - department
    def set_department(self, department):
        self.__department = department

    # getter - salary
    def get_salary(self):
        return self.__salary

    # setter - salary
    def set_salary(self, salary):
        self.__salary = salary
