count = 0
try:
    f = open("Anurag.txt","r")

    for line in f:
        words = line.split()
        for word in words:
            if len(word) < 4:
                count += 1

except:
    print("Unable to read file")

print("Total number of Words whose length is less then 4 is: ",count)
    