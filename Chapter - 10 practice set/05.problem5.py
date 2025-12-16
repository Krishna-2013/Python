from random import randint
class train:
    def __init__(self,TrainNo):
        self.TrainNo = TrainNo

    def book (self, From, To):
        print(f"Train is booked in train number: {self.TrainNo} from {From} to {To}")

    def getstatus (self,):
        print(f"Train number {self.TrainNo} is running on time")

    def getfare (self, From, To):
        print(f"The ticket fare in train number: {self.TrainNo} from {From} to {To} is {randint(222, 2999 )}")

t = train(1522) 
t.book("Dhaka", "Chattogram")
t.getstatus()
t.getfare("Dhaka", "Chattogram")