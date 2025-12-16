class Employee:
    name = "Default name"
    company = "ITC"
    def show(self):
        print(f"The name is: {self.name} and company is: {self.company}")

class coder:
    language = "Python"    
    def printlanguages(self):
        print(f"Out of all languages here is your language: {self.language} ")


class programer(Employee, coder):
    company = "ITC (In For Tech)"
    def showlanguage (self):
        print(f"The name is: {self.name} and he is good in: {self.language}")

a = Employee()
b = programer()

b.show()
b.printlanguages()
b.showlanguage()