tup = (1,2,3,4,5,6,7,8)
print("Tuple is:",tup)
print("Tuple Slicing: ",tup[0:2])


total = tup.count(5)
print("The Total No of Elements: ",total)

max = max(tup)
print("The Max Element in the list is: ",max)

min = min(tup)
print("The Min Element in the list is: ",min)

tup2 = (1,2,3,4,5,6)
result = [i for i in tup if i in tup2]

print("The common Elements are: ",result)