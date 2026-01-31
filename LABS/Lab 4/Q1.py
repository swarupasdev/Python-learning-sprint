li1 = [1,2,4,5,6,7]
print(li1)

print("List Elements entered by loop")
li2 = []
for i in range(1,5):
    element = int(input("Enter the Element: "))
    li2.append(element)

print(li2)

print("Create List using Slicing")
l3 = li1[0:5]
print(l3)