li = [1,2,4,5,6,10]
print(li)
li.append(8)
print("The list after Append: ",li)
li.insert(2,3)
print("The list after Insert: ",li)
li1 = [8,9]
li.extend(li1)
print("The list after extend: ",li)

li.sort()
print("The list after Sorting: ",li)

total = li.count(5)
print("The Total No of Elements: ",total)

max = max(li)
print("The Max Element in the list is: ",max)

min = min(li)
print("The Min Element in the list is: ",min)

pop_ele = li.pop(1)
print("Poped Element is: ",pop_ele)

li.remove(5)
print("List After Remove",li)