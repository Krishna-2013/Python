name = "harry"

# 1. lenth
print(len(name))

# 2. endswith true or false
print(name.endswith("rry"))   #true
print(name.endswith("rrya"))  #false

# 3. starts with true or false
print(name.startswith("ha"))  #true
print(name.startswith("aa"))  #false

# 4. capatilize the first word's first letter
print(name.capitalize())

name2 = "harry is a good boy"

# find the number of the first letter
index = name2.find("is")
print(index)

# replace a word
name_replace = name2. replace("good","bad")
print(name_replace)
