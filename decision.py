#if clause

num=int(input("enter a number: ")) #input() function is used to take input from the user
if num%2==0: print("even number")

#if else clause
num=int(input("enter a number: "))
if num%2==0: print("even number")
else: print("odd number")

#if elif else clause
num=int(input("enter a number: "))
if num==10: print("number is 10")
elif num==20: print("number is 20")
elif num==30: print("number is 30")
else: print("number is not 10, 20 or 30")

#short hand if
num=int(input("enter a number: "))
if num%2==0: print("even number")

#short hand if else
num=int(input("enter a number: "))
print("even number") if num%2==0 else print("odd number")

#short hand if elif else
num=int(input("enter a number: "))
print("number is 10") if num==10 else print("number is 20") if num==20 else print("number is 30") if num==30 else print("number is not 10, 20 or 30")

#nested if
num=int(input("enter a number: "))
if num%2==0:
 if num%3==0: print("number is divisible by 2 and 3")
 else:print("number is divisible by 2 but not 3")
else:print("number is not divisible by 2")


