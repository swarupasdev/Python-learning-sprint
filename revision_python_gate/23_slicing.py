from array import*
emp_id = array("i",[201,202,203,204,205,206,207])
print("original array")
n = len(emp_id)
for i in range(n):
    print(i,'=', emp_id[i])

print("*******************")

new_emp_id=emp_id[1:5:1]
for i in new_emp_id:
    print(i)