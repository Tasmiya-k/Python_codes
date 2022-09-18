class Train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
        self.count=0

    def getstatus(self):
        print(f"the name of train is {self.name} ")

        print(f"the no of seats available are {self.seats} ")
        print("****************")


    def fairinfo(self):
        print(f"the fare of train is {self.count*self.fare} ")
        print("****************")

    def bookticket(self):
        if(self.seats>0):
            print(f"your ticket is booked and your seat no. is {self.seats} ")
            self.seats=self.seats-1
            self.count=self.count+1
        else:
            print("This train is full! Kindly go for Tatkal")

        print("*******************************")

    def cancelticket(self, seatno):
        pass


intercity=Train("intercity: 12554", 90, 2)
intercity.getstatus()
intercity.bookticket()
intercity.bookticket()
intercity.bookticket()
intercity.fairinfo()
intercity.getstatus()
