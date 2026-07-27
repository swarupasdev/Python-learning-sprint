#arithmetic operator
a1 = 4
b1 = 2
print(a1+b1)
print(a1-b1)
print(a1*b1)
print(a1/b1)
print(a1%b1)
print(a1**b1)
print(a1//b1)

#relational operator
a2 = 5
b2 = 3
print(a2>b2)
print(a2<b2)
print(a2==b2)
print(a2!=b2)
print(a2>=a2)
print(b2<=b2)

#logical operator
a3 = 6
b3 = 3
print((a3>b3) and a3<b3)
print((a3<b3) and a3>b3)
print((a3==b3) and a3>b3)
print((a3>b3)and(b3<a3))
print(True and a3)
print(True and a3 and b3)
print(False and b3)

print((a3>b3) or a3<b3)
print((a3<b3) or a3>b3)
print((a3==b3) or a3>b3)
print((a3>b3)or(b3<a3))
print(True or a3)
print(True or a3 or b3)
print(False or b3)

print(not a3<b3)
print(not a3>b3)
print(not a3>b3)
print(not b3<a3)
print(not True)
print(not False)
print(not b3)

#Assignment operator
a4 = 20
a4+=10
b4 = 30
b4-=10
c4 = 40
c4*=10
d4 = 50
d4/=10
e4=60
e4%=10
f4=70
f4**=10
g4=80
g4//=10

print(a4)
print(b4)
print(c4)
print(d4)
print(e4)
print(f4)
print(g4)

#Membership operator
st1="welcome to grim-sage"
print("to"in st1)
print("sex"in st1)
print("sex" not in st1)

#identity operator
a5 = 10
b5 = 10
c5 = '10'

print(id(a5))
print(id(b5))
print(id(c5))

print(a5 is b5)
print(a5 is c5)
print(a5 is not b5)
print(a5 is not c5)
