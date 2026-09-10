from numpy import*
marks = logspace(1, 7, num = 5, endpoint = True , base = 10.0, dtype = None)
n = len(marks)
for i in range(n):
    print("index",i,marks[i])
    i+=1