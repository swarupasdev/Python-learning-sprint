from numpy import*
a = array([100, 200, 350, 400, 500])
b = array([100, 200 , 300 , 250,550])
result = where((a>b), a, b)
print(result)