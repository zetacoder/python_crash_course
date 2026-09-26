'''
11-3. Employee: Write a class called Employee. The _init__() method should take in a first name, a last name, and an annual salary, and store each of these as attributes. 

Write a method called give_raise() that adds $5,000 to the annual salary by default but also accepts a different raise amount.

Write a test file for Employee with two test functions, test_give_default_raise() and test_give_custom_raise(). 

Write your tests once without using a fixture, and make sure they both pass. 

Then write a fixture so you don't have to create a new employee instance in each test function. Run the tests again, and make sure both tests still pass.

'''

from employee import Employee

emp = Employee("abc", "xyz", 200000)

emp_1 = Employee("cdf", "mno", 300000)

emp.give_raise()

emp_1.give_raise(20000)

print(f"Annual Salary for {emp.first_name} is : {emp.annual_salary}")

print(f"Annual Salary for {emp_1.first_name} is : {emp_1.annual_salary}")

