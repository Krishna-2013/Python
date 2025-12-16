Marks = {
    "Krishna": 93,
    "Rijvi": 94,
    "Rife": 87,
}

print(Marks.items()) #all in tuple
print(Marks.keys()) #all names
print(Marks.values()) # all numbers or values
Marks.update({"Krishna": 99, "Sudipto" : 92}) #Change values and also add name
print(Marks)
print(Marks.get("Rimi")) # to get the marks of any name
print(Marks.get("Krishna")) # to get the marks of any name

# print(Marks.get("Krishna2")) # Print None
# print(Marks["Krishna2"]) # Returns an Eror


print(len(Marks))
