freinds = ["Krishna", "Rife", "popcorn", 5 , 5.555, True, False, "Best Friend"]

print(freinds)
freinds.append("Sudipto")
print(freinds)

k = [1, 55, 34, 22, 100, 20 ,38]
k.sort()
print(k)

l = [1, 55, 34, 22, 100, 20 ,38]
l.reverse()
print(l)

n = [1, 55, 34, 22, 100, 20 ,38]
n.insert(3, 212) # index , object
print(n)

c = [1, 55, 34, 22, 100, 20 ,38]
c.pop(3)
print(c)
print(c.pop(3))

v = [1, 55, 34, 22, 100, 20 ,38]

print(v.pop(3)) # same as Value = v.pop(3)  |  print (Value)

z = [1, 55, 34, 22, 100, 20 ,38]
z.remove(100)
print(z)