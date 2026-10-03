from numpy import*
array1 = array([[10, 20, 30, 40],
                [50, 60, 70, 80]])

#without index
for r in array1:
    for s in r:
        print(s)
    print()

n = len(array1)
for i in range(n):
    for j in range(len(array1[i])):
        print(array1[i][j])
