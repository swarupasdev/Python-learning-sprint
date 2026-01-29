#set
#immutable=unchangable, use {} for set, set is hetrogeneouse means string, number etc
#set removes the duplicate values
set1={1,2,1,3,4,5}
print(set1)

my_set={1.0,"hello",(1,2,3)} #set of mixed datatypes
print(my_set)

my_set=set([1,2,3,2]) #using set function
print(my_set)

my_set={1.0,"hello",(1,2,3)} #length 
print(len(my_set))

set1={1,2,1,3,4,5} #type
print(type(set1))

set1=set((1,2,1,3,4,5)) #set() constructor converts the tuple or list into set
print(set1)

#to create empty set use set() if we take a={} the the answer will be dictionary bcoz dictionary and set are denoted by {}
a={}
print(type(a)) # o/p dictionary

a=set()
print(type(a)) #o/p set

# Python example demonstrate that a set can store heterogeneous elements
myset = {"Geeks", "for", 10, 52.7, True} #every time different o/p
print(myset)


#access items
set={"apple","mango","banana"} #all the elements are printed
for x in set:
    print(x)

print("banana" in set) #true

#add item
set={"apple","mango","banana"}
set.add("orange")
print(set)

set1={"apple","mango","banana"}
set2={"cherry","papaya","papaya"}
set1.update(set2)
print(set1)

#remove raises error if the item does not found in the set and the program will break
set={"apple","mango","banana"}
set.remove("mango")
print(set)

#set={"apple","mango","banana"}
#set.remove("orange") #error arrises
#print(set)

#discard does raise error if the item does not found in the set and the program will be processed
set={"apple","mango","banana"}
set.discard("orange")
print(set)

set={"apple","mango","banana"}
set.discard("orange") #no error arrises
print(set)

#del is used to delete the item in the set
#set={"apple","mango","banana"}
#del set #error will be arrise bcoz the set is deleted
#print(set) 

#join two sets
set1={"a","b","c"} #union will add both the sets it will give new set in output by assiging new set
set2={1,2,3}
set3=set1.union(set2)
print(set3)

set1={"a","b","c"} #update will add items in the given set
set2={1,2,3}
set1.update(set2)
print(set1)  