thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict['color']="red" #adding
thisdict.pop("model") #removing
thisdict.popitem() #removing the last inserted item
thisdict.clear() #empties the dictionary
#del thisdict #empties the dictionary
print(thisdict)

thisdict ={
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#Print all key names in the dictionary, one by one:
for x in thisdict:
  print(x)

#Print all values in the dictionary, one by one:
for x in thisdict:
  print(thisdict[x])
  
  thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)

#Copy a Dictionary
t = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
m = t.copy() 
print(m)

