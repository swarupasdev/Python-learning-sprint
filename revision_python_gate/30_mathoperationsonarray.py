from numpy import*
a = array([101, 102, 103, 104, 105])
a = a+5
print(a)
b = array([201, 202, 203, 204, 205])
c = array([301, 302, 303, 304, 305])
d = b + c
i = 0
for el in d:
    print("index",i,el)
    i+=1
