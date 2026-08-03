for i in range(5):
    print(i)
    if i>=3:
     break
print("rest of the code")

for j in range(1,20,3):
    if j>=10:
        continue  #means if the condition satisfy continue to skip and print the unsatisfied
    print(j)
print("rest of the code")
