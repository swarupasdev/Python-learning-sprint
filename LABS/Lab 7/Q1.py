#Sum of List of Elements using Map function 

# li = [1,2,3,4,5]
# sum = 0

# def addition(n):
#     global sum
#     sum = sum + n

# list(map(addition,li))
# print(sum)


#Sum of List items using Lambda Function

from functools import reduce

li = [1,2,3,4,5]
total = reduce(lambda x, y: x + y, li)
print(total)