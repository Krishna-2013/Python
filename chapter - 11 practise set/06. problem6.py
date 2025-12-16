class Vector:
    def __init__ (self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result
    
    def __str__(self):
        return f"{self.x}i + {self.y}j + {self.z}k)"
    
# Test the impliment
V1 = Vector(1, 2, 3)
V2 = Vector(4, 5, 6)
V3 = Vector(7, 8, 9) # Same dimention vector

print(V1 + V2) # Output Vector(5, 7, 9)
print(V1 * V2) #Output: 32
