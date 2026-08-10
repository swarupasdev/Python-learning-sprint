from array import*
stu_roll = array('i',[])
n = int(input("Enter number of Elements:"))

for i in range(n):
    stu_roll.append(int(input("Enter Element: ")))

for i in range(len(stu_roll)):
    print(stu_roll[i])

#using while loop

from array import*
emp_id = array("i",[])
m = int(input("Enter number of element: "))

j = 0
k = 0
while j<m:
    emp_id.append(int(input("enter your element: ")))
    j+=1

while j<len(emp_id):
    print(emp_id[j])
    j+=1