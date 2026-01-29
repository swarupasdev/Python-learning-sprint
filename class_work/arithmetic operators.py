a=2
b=5
print(a*b) #simple multiply
print(a**b) #b is the power of a when we 2*2*2*2*2 = 32

print(a/b) #it takes the quotient full value after the decimal as well
print(a//b) #it takes the quotient before the decimals

print(b/a)
print(b//a)

print(b%a)

str1=input("Enter a string: ")
str2=input("Enter a string to find it is in string 1 or not: ")
if str2 in str1:
    print(str2, "Found in the string")
else:
    print(str2, "String is not found")