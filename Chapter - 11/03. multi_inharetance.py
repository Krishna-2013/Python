class Employee:
    a = 1

class Programer(Employee):
    b = 2

class Manager(Programer):
    c = 3

# o = Employee()
# print(o.a) #Prints the "a" attribute
# print(o.b) #prints an eror because there is no "b" attributr in the class


o = Programer()
print(o.a)
print(o.b)
# print(o.c) #prints an eror because there is no "c" attributr in the class

o = Manager()
print("\n",o.a)
print(o.b)
print(o.c)