from array import *

stu_mark = array('i', [40, 50, 60, 70, 80])
n = len(stu_mark)
i = 0
while i<n:
    print(stu_mark[i])
    i+=1
print("After array reverse")
stu_mark.reverse()
n = len(stu_mark)
i = 0
while i<n:
    print(stu_mark[i])
    i+=1

