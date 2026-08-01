#while loop:

a = 1
while a <= 10:
    print(a)
    a+=1
print("finished")

b = 6
while b<=5:
    print(b)
    b+=1
else:
    print("while condition false else run")
print("rest of the code")    

i = 0
while True:
    i += 1
    print(i)
    if(i == 3):
        break
print("rest of the code")

j = 1 
while j <= 3:
    print("outer loop", j)
    j+=1
    k=1
    while k<= 5:
        print("Inner loop",k)
        k+=1
print("rest of code")        