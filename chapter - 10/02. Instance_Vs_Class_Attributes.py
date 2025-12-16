class Employee:
    language = "Python" #This is a class attribute
    salery = 1200000  #This is a class attribute

    def getinfo(self):
        print(f"The language is: {self.language}, and the salery is: {self.salery}")

    def greet(self):
        print("Good morning")

harry = Employee()
harry.language = "Javascript"  #This is an instance attribute
print(harry.language, harry.salery)

Employee.greet(harry)
Employee.getinfo(harry)
