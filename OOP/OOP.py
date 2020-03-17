# Notes on Object Oriented Programming in Python - According to Corey Schafer

class Employee:

    raise_amount = 1.04 # Class Variable
    num_of_emps = 0
    
    # Constructor
    def __init__(self, first, last, pay): # Instance is first argument, these are all attributes (do not need parentheses when called)
        self.first = first # Could be fname in self.fname but easier this way
        self.last = last # These are known as instance variables or properties or attributes
        self.pay = pay
        self.email = first + "." + last + "@company.com"

        # Since running every time we create a new employee, we can increment num_of_emps each time one is created
        Employee.num_of_emps += 1 # Using class instead of self because there is no real use case where we would want num_of_emps to be different for any one instance

    # This is known as a method (function - needs parentheses when called)
    def fullname(self): # Do not leave self out, if you leave it out you will get error about taking arguments because it is passed automatically
        return print("{} {}".format(self.first, self.last))
        
    def apply_raise(self):
        # If Employee class not referenced in class variable Employee.raise_amount will get an error (can also use instance to acces by using self.raise_amount which is preferred)
        # Using self is using the instance, gives us ability to change amopunt for single instance if wanted to (for single employee), and allow any subclass to override thise constant if desired
        self.pay = int(self.pay * self.raise_amount) 

    @classmethod # working with class instead of instance
    def set_raise_amount(cls, amount): # cls is convention such as self, cant use Class
        cls.raise_amt = amount


# Main Tests
def main():

    # Each employee we create will be an instance of that class
    emp_1 = Employee()
    emp_2 = Employee()

    print(emp_1) # Prints Memory
    print(emp_2) # Prints Memory

    # Manually set attributes
    emp_1.first = "Ryan"
    emp_1.last = "Kohanski"
    emp_1.email = "Ryan.Kohanski@company.com"
    emp_1.pay = 50000

    emp_2.first = "Test"
    emp_2.last = "User"
    emp_2.email = "Test.User@company.com"
    emp_2.pay = 60000

    print(emp_1.email)
    print(emp_2.email)

    # Use class for attributes, manual assignments now irrelevant
    emp_1 = Employee("Ryan", "Kohanski", 50000) # Emp_1 passes in as self while rest correspond
    emp_2 = Employee("Test", "User", 60000) # Emp_2 passes in as self while rest correspond

    print(emp_1.email)
    print(emp_2.email)

    # This is a lot to type to print full name, so make a method/function to do it
    print("{} {}".format(emp_1.first, emp_1.last))
    print(emp_1.fullname()) # Same thing

    # Background
    print(Employee.fullname(emp_1)) # This is what the line below translates to
    print(emp_1.fullname()) # Similar lines, do same thing, difference is what to pass in

    # Raises Manually, cannot access raise amount here, attribute does not exist, cannot update this amount, could be all over the place
    print(emp_1.pay)
    emp_1.apply_raise()
    print(emp_1.pay)

    # Using a class variable
    print(Employee.raise_amount)
    print(emp_1.raise_amount)
    print(emp_2.raise_amount)
    print(emp_1.__dict__) # Does not show amount
    print(Employee.__dict__) # Does show amount
    
    Employee.raise_amount = 1.05 # Changes for class and all instances using class
    emp_1.raise_amount = 1.05 # Change using instance instead of class (changes only for emp_1)

    # Number of Employees
    print(Employee.num_of_emps)
    # If I create an employee like: emp_1 = Employee("Ryan", "Kohanski", 50000), then print, the count will increase

    # Class Methods
    emp_1 = Employee("Ryan", "Kohanski", 50000) 
    emp_2 = Employee("Test", "User", 60000) 

    Employee.set_raise_amount(1.05) # or
    emp_1.set_raise_amount(1.05)

    print(Employee.raise_amount)
    print(emp_1.raise_amount)
    print(emp_2.raise_amount)

    



    
main()








