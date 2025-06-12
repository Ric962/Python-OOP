# initiate a class
class Employee:

    # special method/magic method/dunder method - constructor
    def __init__(self):
        print("Started executing attribute")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("Attributes has been initiated")
    
    def travel(self, destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")

# create an object/instance of the class
richard = Employee()

# printing the attribute
print(richard.salary)

# calling the method
richard.travel("New York")