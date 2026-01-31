count = 0

try:
    f = open("Anurag.txt","r")

    for line in f:
        if not line.startswith("A"):
            count+=1
except:
    print("Unable to Open file")

print("Number of lines not starting with A: ",count)