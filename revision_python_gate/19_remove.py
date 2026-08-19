from array import*
emp_id = array('i',[101,102,103,104,105])
n = len(emp_id)
i = 0
while i<n:
    print(emp_id[i])
    i+=1
print("Array after remove")
emp_id.remove(101)
n = len(emp_id)
i=0
while i<n:
    print(emp_id[i])
    i+=1

