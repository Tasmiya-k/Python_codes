class programmer:
    Company="Microsoft"               #class atrribute

    def __init__(self, name, product):
        self.name=name
        self.product=product


    def getinfo(self):
        print(f"the name of {self.Company} programmer is {self.name} and the product is {self.product} ")
        #print(f"the name of programmer is {self.name}")


Tasmiya=programmer("tasmiya", "webpage")
Neha=programmer("neha", "designer")
Rahul=programmer("rahul", "manager")

Tasmiya.getinfo()
Neha.getinfo()
Rahul.getinfo()