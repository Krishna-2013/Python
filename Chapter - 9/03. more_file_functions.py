# Read lines function

f = open("file.text")
lines = f.readlines()

print(lines, type(lines))
f.close()

# Read line function

# f = open("file.text")
# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))
# f.close()

f = open("file.text")
line = f.readline()
while(line != ""):
    print(line, end = "")
    line = f.readline()

f.close