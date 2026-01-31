String = str(input("Enter the String: "))
l = String.split()
new = ""
for i in range(len(l)-1):
    String = l[i]
    new += (String[0].upper()+'.')
new+= l[-1].title()

print(new)