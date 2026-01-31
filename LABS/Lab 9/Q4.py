count = 0
try:
    f = open("Anurag.txt","r")

    for line in f:
        words = line.split()
        count += len(words)

except:
    print("Unable to read file")

print("Total number of Words: ",count)
    