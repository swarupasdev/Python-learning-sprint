from numpy import*
crazy = ones(5, dtype = int, order = 'F')

n = len(crazy)
for i in range(n):
    print('index',i,crazy[i])
    i+=1
