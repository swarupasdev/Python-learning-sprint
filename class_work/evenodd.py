#even odd
num = int(input("Enter a number: "))
if num%2==0:
    print(num, "is even")
else:
    print(num, "is odd")
    
#area of circle
pi=7.14
r=int(input("enter the value of radius: "))
area=pi*r**2
print("Area of circle is", area)

#area of rectangle
l=int(input("Enter the length of rectangle: "))
b=int(input("Enter the breadth of rectangle: "))
area=l*b
print("The area of rectangle is", area)

#number checker
num = int(input("Enter a number: "))
if num==10:
    print("The number is equal to 10")
elif num==50:
    print("The number is equal to 50")
elif num==100:
    print("The number is equal to 100")
else:
    print("Number is not equal to 10, 50, 100")

#short hand if else    
a = 2
b = 330
print("A") if a > b else print("B")

#nested if
num=int(input("Enter a number: "))
if num>10:
    print("The number is greater than 10")
    if num>20:
        print("The number is greater than 20")
    else:
        print("The number is smaller than 20")
else:
    print("The number is smaller than 10")