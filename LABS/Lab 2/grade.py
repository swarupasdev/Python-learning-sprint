num1 = int(input("Enter Numebr 1: "))
num2 = int(input("Enter Numebr 2: "))
num3 = int(input("Enter Numebr 3: "))
num4 = int(input("Enter Numebr 4: "))
num5 = int(input("Enter Numebr 5: "))

avg = (num1+num2+num3+num4+num5)/5

if(avg>90):
    print("Your Grade is O")
elif(avg>=81 and avg<=90):
     print("Your Grade is A+")
elif(avg>=71 and avg<=80):
     print("Your Grade is A")
elif(avg>=61 and avg<=70):
     print("Your Grade is B+")
elif(avg>=51 and avg<=60):
     print("Your Grade is B")
elif(avg>=41 and avg<=50):
     print("Your Grade is C+")
elif(avg>=35 and avg<=40):
     print("Your Grade is C")
else:
     print("You are Fail !!!")