
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end="")
    print()

# for i in range(1,5):
#     for j in range(5, i, -1):
#         print(" ",end="")
#     for j in range(i,1,-1):
#         print(j,end="")
#     for j in range(1, i+1):
#         print(j, end="")
#     print()

for i in range(1,6):
    for j in range(1,i):
        print(" ",end="")
    for j in range(i,6):
        print(j,end="")
    print()