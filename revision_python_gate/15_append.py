from array import*
stu_roll=array('i',[101,102,103,104,105])
m = len(stu_roll)
k = 0
while k<m:
    print(stu_roll[k])
    k+=1

print("Array after append")
stu_roll.append(106)
l = len(stu_roll)
p = 0
while p<l:
    print(stu_roll[p])
    p+=1