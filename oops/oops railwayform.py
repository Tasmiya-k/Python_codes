

class RailwayForm:
    Formtype="RailwayForm"
    def printData(self):
        print(f"Name is{self.name}")
        print(f"Train is{self.train}")

harryapplication=RailwayForm()
harryapplication.name=input("Enter your name ")
harryapplication.train=input("Enter your train name ")
harryapplication.trainnumber=input("Enter train number ")
harryapplication.printData()