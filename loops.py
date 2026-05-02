#loops
#while loop
'''
i=1
while i<5:
    print("hello")
    i=i+1
#while(1):
 #  print("hello")

#for loop

for i in range(1,5): #range(5) means 0 to 4
                     #range(1,5) means 1 to 4
                     #range(1,5,2) means 1 to 4 with step 2 i.e 1,3
   print("hello")

str="hello"
for i in str:
    print(i)
    
n=int(input("enter a number"))
n>11
for i in range(1,11,2):
    
    c=i*n
print(i,"*",n,"=",c)

#even numbers
n = int(input("Enter the number "))
for i in range(2,n,2):
 print(i)
 
#odd numbers
n = int(input("Enter the number "))
for i in range(1,n,2):
   print(i)
   '''
#prime numbers
n = int(input("Enter the number "))
for i in range(2,n):
   if(n%i==0):
        print("not prime")
        break
   else:
      print("prime")
      break
  
   '''
#nested for loop
for i in range(1,5):
   for j in range(1,5):
        print(i,j)
        '''