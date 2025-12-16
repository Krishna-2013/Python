class Demo:
    a = 4

o = Demo()

print(o.a)#It prints class attribute because there are instamce attribute is not present


o.a = 0 #instance attribute is set

print(o.a)#It prints instance attribute because there are instamce attribute is present