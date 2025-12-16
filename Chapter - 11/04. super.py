class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programer(Employee):
    def __init__(self):
        print("Constructor of Programer")
    b = 2

class Manager(Programer):
    def __init__(self):
        super().__init__()  #Prints the functions of the parental constructor
        print("Constructor of Manager")
    c = 3

# o = Employee()
# print(o.a)


# o = Programer()
# print(o.a)
# print(o.b)


o = Manager()
print(o.a)
print(o.b)
print(o.c)