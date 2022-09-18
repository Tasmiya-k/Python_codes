class Employee:
    Company="Google"
    def getSalary(self):
        print(f"salary of this employee working in {self.Company} is {self.salary}")

    @staticmethod                #when self is not passed
    def greet():
        print("Hello Good Morning Sir")


tasmiya=Employee()
tasmiya.salary=10000
tasmiya.getSalary()

Employee.getSalary(tasmiya)       #its same as tasmiya.getSalary

tasmiya.greet()
