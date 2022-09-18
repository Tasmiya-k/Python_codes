class calculator:
    def __init__(self,num):
        self.number=num

    def square(self):
        print(f"the square of {self.number} is {self.number **2} ")

    def squareroot(self):
        print(f"the squareroot of {self.number} is {self.number **0.5}" )

    def cube(self):
        print(f"the cube of the {self.number} is {self.number **3}")

    @staticmethod
    def greet():
        print("***Welcome to the best calculator of the world***")

a=int(input("enter number "))
ans=calculator(a)
ans.greet()
ans.square()
ans.cube()
ans.squareroot()


