with open("this.txt", "r") as f:
    content = f.read()

with open("this_coppy.txt", "w") as f:
    f.write(content)