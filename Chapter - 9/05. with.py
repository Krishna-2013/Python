f = open("file.text")
print(f.read())
f.close

#The same can be written by with statement like this:
print("\n")
with open("file.text") as f:
    print(f.read())