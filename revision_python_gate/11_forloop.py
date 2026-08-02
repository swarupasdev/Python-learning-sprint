str1 = 'grim-sage'
for var1 in str1:
    print(var1)
print("rest of the code")

a1 = range(5)
for i in a1:
    print(i)
print("rest of the code")

str2 = 'distance'
rng1 = len(str2) #len() is used to know the length of the expression
for var2 in range(rng1):
    print(var2,"=",str2[var2])
print("rest of the code")

str3 = "microwave"
for var3 in str3:
    print(var3)
else:
    print("else part")
print("rest of code ")

for i1 in range(2):
    print("outer loop", i1)
    for j1 in range(3):
        print("inner loop",j1)
print("rest of code")