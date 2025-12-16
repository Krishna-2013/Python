
# Static_method

class Employee:
    language = "Python" #This is a class attribute
    salery = 1200000  #This is a class attribute

    @staticmethod
    def getinfo():
        print(f"The language is: {Employee.language}, and the salery is: {Employee.salery}")

    @staticmethod
    def greet():
        print("Good morning")

harry = Employee()
harry.language = "Javascript"  #This is an instance attribute
print(harry.language, harry.salery)

harry.greet()
harry.getinfo()
