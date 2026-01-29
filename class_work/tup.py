thistuple = (1,3,7,8,7,5,4,6,8,5)
x = thistuple.count(2) #tells how many times the value is repeated
print(x)

x = thistuple.index(2) #raises exception if not found in tuple
x = thistuple.index(7) 
print(x)