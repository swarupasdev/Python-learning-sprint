#set is unordered  and unchanged collection of unique elements
#set is mutable
#set is unordered
#set is unindexed
#set is unchangeable
myset= {1,2,3,4,5,6,7,8,9,10}
print(myset)
print(type(myset))
# myset.add(11)
# print(myset)
# myset.update([12,13,14,15])
# print(myset)
# myset.remove(15)
# print(myset)
# myset.discard(14)
# print(myset)
# myset.pop()
# print(myset)
# myset.clear()
# print(myset)
# del myset
# print(myset)

#set() constructor
soumi=set(('soumya','soumik','souvik','soumalya'))
print(soumi)
print(type(soumi))

#accesing set items
for x in soumi:
    print(x)
    print("soumya" in soumi)
    
#null set
s=set()
print(s)

shutup={"fack off","get lost","go to hell"}
shutup.add("shut up")
print(shutup)

shutup.update({"motherfucker"})
print(shutup)

shutup.remove("go to hell")
print(shutup)

shutup.discard("tototo")
print(shutup)

# del shutup
# print(shutup)

set1={1,2,3,4}
set2={"x","y","z",}
set3=set1.union(set2)
print(set3)

set1.update(set2)
print(set1)

set7={"kiss","hug","neck"}
set4={"kiss","hug","neck","eat","x"}
set7.intersection_update(set4)
print(set7)