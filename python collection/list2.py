#list
values=[1,2,3,4,5]
print(values)
values[0]=9 #manipulating indices
print(values)

#allowing duplicate
thislist=["apple","banana","cherry","apple","apple"]
print(thislist)

#list length
print(len(thislist))

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
print(list4)
print(type(list2))
print(list1[1])

#deletation
print(list1)
del list1[2]
print("after deletating value at index 2: ")
print(list1)

#remove() method
print(list1)
list1.remove("banana")
print("after removing banana: ")
print(list1)