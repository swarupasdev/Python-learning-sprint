num=int(input("Enter the value: "))
for row in range (1,num+1):
    for col in range (1,row+1):
        print("*", end=" ")
    print()