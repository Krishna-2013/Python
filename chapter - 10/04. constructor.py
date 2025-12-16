class Employee:
    language = "Python" #This is a class attribute
    salery = 1200000  #This is a class attribute

    def __init__(self, name, language, salery):
        self.name = name
        self.language = language
        self.salery = salery
        print("I am creating an object") #Dunder method that call automatically

    def getinfo(self):
        print(f"The language is: {self.language}, and the salery is: {self.salery}")

    def greet(self):
        print("Good morning")

harry = Employee("Harry", "Javascript", 120000)

print(harry.name, harry.language, harry.salery)