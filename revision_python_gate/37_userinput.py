from numpy import*
n = int(input("Enter number of elements: "))
a = zeros(n, dtype=int)
for i in range(len(a)):
    x = int(input('Enter element: '))
    a[i] = x

print(a)