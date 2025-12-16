# Here name is instance attribute and salery and language are class atribute as they directly belong to the class

class Employee:
    language = "py" #This is a class attribute
    salery = 1200000  #This is a class attribute

harry = Employee()
harry.name = "Harry"  #This is an instance attribute
print(harry.name, harry.language, harry.salery)

rohan = Employee()
rohan.name = "Rohan"
print(rohan.name, rohan.salery, rohan.language)