f = open("poem.text")
C = f.read()
if ("Twinkle" in C):
    print("Twinkle is present in the content")

else:
    print("Twinkle is not present in the content")
f.close()