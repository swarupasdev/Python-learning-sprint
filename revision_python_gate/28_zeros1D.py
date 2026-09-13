from numpy import*
crazy = zeros(5, dtype = int, order = 'F')

n = len(crazy)
for i in range(n):
    print('index',i,crazy[i])
    i+=1
