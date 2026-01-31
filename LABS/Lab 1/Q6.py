num1 = int(input("Enter the Number 1: "))
num2 = int(input("Enter the Number 2: "))
exp = input("Enter the Operation: ")

if(exp == "+"):
    print("The sum is: ",num1+num2)
elif(exp == '*'):
    print("The Multiply is: ",num1*num2)
elif(exp == '-'):
    print("The Substraction is: ",num1-num2)
elif( exp == '/'):
    print("The Division is: ",num1/num2)
else:
    print("Enter Valid Number")