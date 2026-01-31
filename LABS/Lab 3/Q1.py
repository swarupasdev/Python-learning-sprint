num = int(input("Enter the Number: "))
if(num%2 ==0):
    print(num, " is even Number")
else :
    print(num," is odd Number")
c=0
for i in range(2,int(num/2)):
    if(num%i == 0):
       c+=1
       break
    
if(c==0):
    print("The Number a Prime Number ")
else:
    print("The Number is not a prime Number")
