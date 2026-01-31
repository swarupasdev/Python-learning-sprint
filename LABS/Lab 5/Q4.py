li = []


for i in range(1,51):
    counter = 0
    if(i == 1):
        continue
    for j in range(2,i):
        if(i%j==0):
            counter += 1
            break
    if(counter == 0):
        li.append(i)

print("The Prime Numbers between 1 to 50 are: ",li)