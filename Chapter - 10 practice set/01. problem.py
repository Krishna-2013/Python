class programer:
    Company = "Microsoft"
    def __init__(self, name, salery, pincode):
        self.name = name
        self.salery = salery
        self.pincode = pincode

p = programer("Krishna", 540000, 1234)

print(p.Company, p.name, p.salery, p.pincode)