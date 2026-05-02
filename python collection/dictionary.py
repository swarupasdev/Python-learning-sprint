thisdict={"brand":"ford", "model":"mustang", "manf":"1969"}
print(thisdict)
print(len(thisdict))
print(type(thisdict))

d1={"key":1,"lock":2,"hook":3}
print("key=", d1["key"])
print("lock=", d1.get("lock"))

#manipulate and add
dict1={"key":1,"lock":4,"draw":9}
dict1["clip"]=5 #add
dict1["key"]=6
print(dict1)
dict1.pop("key")
print(dict1) #pop()

# del dict1
# print(dict1)

soumi={"nature":"sarcastic","attitude":"sweet","behaviour":"responsible"}
soumi.clear()
print(soumi)

swarup={"nature":"good","attitube":"egoistic", "behaviour":"kindhearted"}
for x in swarup:
    print(x)
    print(swarup[x])

    
for x,y in swarup.items():
    print(x,y)
    
#copy()
dona=swarup.copy()
print(dona)

dona=dict(swarup)
print(dona)

#formkey()
blue=("color","breed","age")
attr=0
dog=dict.fromkeys(blue,attr)
print(dog)

#keys()