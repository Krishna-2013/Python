s1 = {7, 10, 6, 5}
s2 = {10, 0, 3, 2}

print(s1.union(s2)) #combine all sets without any repitation
print(s1.intersection(s2))

s4 = {9, 1, 3, 6, 5, 2}
s5 = {9, 1, 3, 6}
print(s4 - s5) # remove yhe same numbers

print(s4.issuperset({5,6})) #True
print(s4.issuperset({5,7})) #False

