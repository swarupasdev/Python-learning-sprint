#user input for no. of rows
rows=int(input("Enter the rows: "))
#outer loop will print the no. of rows
for i in range(0,rows+1):
# Inner loop will print number of Astrisk
 for j in range(i):
  print("*",end = '')
print()