#break
i=-1
while(i<6):
    if(i==3): 
        break
    i+=1 
    print(i)

var = 10 # Second Example
while var > 0: 
    print ('Current variable value :', var)
    var = var -1
    if var == 5:
        break
print ("Good bye!")


var = 10 # Second Example
while var > 0: 
    var = var -1
    if var == 5:
        continue
    print ('Current variable value :', var)
print ("Good bye!")

i = 1
while i < 6:
    i += 1
    if i == 3:
        continue
print(i)

#table
n=int(input("Enter a value for which you need table to be printed: "))
for i in range(1,11):
    table=n*i
    print(n, "*", i, "=", table)    

#printing even numbers
n = int(input("Enter the number "))
for i in range(2,n,2):
    print(i)
  
list=['nandini', 'Vipul', 'Kirti']    
for i in range (len(list)):
    print("Hello", list[i])
    
rows = int(input("Enter the rows: "))
for i in range(0,rows+1):
    for j in range(i):
        print(i,end = '')
print()

#loop
for i in range(0,5):
    print(i)
else:
    print("for loop completely exhausted, since there is no break.")

for letter in 'Python': # First Example
    if letter == 'h':
        break
print ('Current Letter :', letter)
