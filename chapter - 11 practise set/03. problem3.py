class Employee:
    salery = 234
    increament = 20

    @property
    def SaleryAfterIncreament(self):
        return (self.salery + self.salery * (self.increament/100))
    
    @SaleryAfterIncreament.setter
    def SaleryAfterIncreament(self, salery):
        self.increament = ((salery/self.salery) - 1) * 100

    
e = Employee()
print(e.SaleryAfterIncreament)