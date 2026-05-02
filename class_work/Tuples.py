tup=('rakesh',23,6.2,False)
print(tup[0])
print(tup[-4])


#assignment dont done
#tup_num=(1,2,3,4)
#tup_num[2]=(5)

thistuple =("apple","banana","cherry","apple","cherry")
print(thistuple)

thistuple =("apple","banana","cherry","apple","cherry")
print(len(thistuple)) #length of tuple

thistuple = ("apple",)
print(type(thistuple))

thistuple = ("apple") #since the tuple have single value it is supposed to have a comma  
print(type(thistuple))

T1=(1,2,3,4) #repetition
print(T1*2)

T1=(1,2,3,4) #concatenation
T2=(5,6,7,8) 
print(T1+T2)

T1=(1,2,3,4) #Membership
print(2 in T1) #ans True

T1=(1,2,3,4) #Membership
print(5 in T1) #ans False

T1=(1,2,3,4) #Iteration
for i in T1:
   print(i) 

thistuple = (1,3,7,8,7,5,4,6,8,5) #count() method returns the number of times a specified value appears in the tuple
x = thistuple.count(5)
print(x) 

thistuple = (1,3,7,8,7,5,4,6,8,5) #index method finds the first occurrence of the specified value.
x = thistuple.index(7)
print(x)
