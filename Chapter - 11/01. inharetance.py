class Employee:
    company = "ITC"
    def show (self):
        print(f"The name is: {self.name} and salery is: {self.salery}")
    
# class programer:
#     company = "ITC (In For Tech)"
    # def show (self):
    #     print(f"The name is: {self.name} and salery is: {self.salery}")
    
#     def showlanguage (self):
#         print(f"The name is: {self.name} and he is good in: {self.language}")

# It canbe
class programer(Employee):
    company = "ITC (In For Tech)"
    def showlanguage (self):
        print(f"The name is: {self.name} and he is good in: {self.language}")

a = Employee()
b = programer()

print(a.company, b.company)