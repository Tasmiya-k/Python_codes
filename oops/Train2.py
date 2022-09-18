class Train:
    def __init__(self,name):
        self.name=name
        self.fare=0
        self.seats=0
        self.num=0

    def getstatus(self):

        if(self.name=="intercity"):
            self.fare=300
            self.seats=2

        elif(self.name=="Rajhdhani"):
            self.fare=500
            self.seats=3


        print(f"the name of train is {self.name} ")
        print(f"the no of seats available are {self.seats} ")


    def fairinfo(self):
        print(f"the fare of train is {self.fare*self.num} ")

    def bookticket(self):
        if(self.seats>0):
            print(f"Your ticket is book and your seat no is {self.seats} ")
            self.seats=self.seats-1
            self.num=self.num+1

        else:
            print("       Sorry the train is full! Kindly go for Tatkal   ")




name=input("enter the name of train ")
intercity=Train(name)
intercity.getstatus()
intercity.fairinfo()
intercity.bookticket()
intercity.bookticket()
intercity.bookticket()
intercity.getstatus()
