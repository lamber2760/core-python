from random import randint

class Train:
    def __init__(self,tarinNo):
        self.trainNo = tarinNo

    def book(self,fro,to):
        print(f"Ticket is booked in train no :{self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"Train no : {self.trainNo} is running on time")

    def getfare(self,fro,to):
        print(f"Ticket fare in train no :{self.trainNo} from {fro} to {to} is {randint(222,5555)}")     

t =Train(12421)
t.book("kangra","chandigarh")   
t.getfare("rampur","bilaspur")
t.getstatus()             