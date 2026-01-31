string = str(input("Enter the String: "))
length = len(string)
for i in string:
    print(i,end="")
print()
while(length>0):
    print(string[length-1], end="")
    length = length-1