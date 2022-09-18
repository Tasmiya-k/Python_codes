class Employee:
    Company="Google"


    def __init__(self, name, salary,subunit ):                     #constructor
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Employee is created")

    def getDetails(self):
        print(f"the name of the employee is {self.name}")
        print(f"the salary of the employee is {self.name}")
        print(f"the subunit of the employee is {self.name}")

tasmiya=Employee("tasmiya",1000, "JR dev")
tasmiya.getDetails()