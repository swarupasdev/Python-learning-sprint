from array import*
stu_id = array('i',[101,102,103,104,105])
arr1 = array('i',[106,105,108, 109])
n = len(stu_id)
i = 0
while i<n:
    print(stu_id[i])
    i+=1

print("Array after extend")
stu_id.extend(arr1)
n=(len(stu_id))
i = 0
while i<n:
    print(stu_id[i])
    i+=1