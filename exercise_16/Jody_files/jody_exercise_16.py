# client script

from person import Person
from employee import Employee
from customer import Customer

# how would we be using this? Possible use cases:
# 1 - create a new customer record when they make first purchase
# 2 - update customer record when they make a subsequent purchase
# 3 - create new employee record when they start
# 4 - update employee record (pay rise, job change etc.)
# should this be two different interfaces? a customer based one and an employee based one?


person_1 = Person("Greg", "Davies")
print(person_1.get_person_name())
print(person_1.fullname())

print("Person records created: ", Person.num_created)

employee_1 = Employee("Jody", "Broad", "Python Developer", "IT", 25000)
print(employee_1.get_person_name())
print(employee_1.get_department())
print(employee_1.get_job_title())
print(employee_1.get_salary())

print("Employee records created: ", Employee.num_of_employees)


customer_1 = Customer("Mike", "Wozniak", "moustache wax", 15, "Email only")
print(customer_1.get_person_name())
print(customer_1.get_purchase_history())
print(customer_1.get_loyalty_points())
print(customer_1.get_marketing())

print("Customer records created: ", Customer.num_of_customers)
