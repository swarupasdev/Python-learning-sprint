from numpy import*
a = array([100, 200, 300, 400, 500])
b = array([10, 20 , 30 , 40 , 50])
c = array([100, 20 , 300 , 40 , 50])
d = array([100, 200, 300, 400, 500])

result = a == b
result1 = b == c
result2 = a ==d

print(result)
print(any(result))
print(any(result1))
print(all(result))
print(all(result2))