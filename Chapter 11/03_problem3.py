# # Create a class ‘Employee’ and add salary and increment properties to it.
# # Write a method ‘salaryAfterIncrement’ method with a @property decorator
# #  with a setter which changes the value of increment based on the salary.

class Employee:
    salary = 234
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return self.salary + self.salary * (self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        self.increment = ((new_salary / self.salary) - 1) * 100

# Create an instance of the Employee class
e = Employee()

# Set the new salary after increment
e.salaryAfterIncrement = 280.8

# Print the updated increment
print(e.salaryAfterIncrement)


