try:
    f = open("Anurag.txt","r")
    for line in f:
        print(line)
except:
    print("Unable to Open File")