# stu1_roll = 101
# stu2_roll = 102
# stu3_roll = 103
# stu4_roll = 104
# stu5_roll = 105

# print(stu1_roll)
# print(stu2_roll)
# print(stu3_roll)
# print(stu4_roll)
# print(stu5_roll)

# # Create a 1D list
# my_list = [10, 20, 30, 40, 50]
#
# # Access elements (using 0-based indexing)
# print(my_list[0])   # Output: 10
# print(my_list[-1])  # Output: 50 (last element)
#
# # Modify an element
# my_list[1] = 25     # Changes 20 to 25
#
# # Add an element to the end
# my_list.append(60)
#

import array
stu_roll = array.array("i",[ 101,102,103,104,105])
print(stu_roll[0])

print(stu_roll)

#accessing array with for loop
from array import*
emp_num=array("i",[102, 102,103,104,105])

for element in emp_num:
    print(element)

n = len(emp_num)
for i in range(n):
    print(emp_num[i])