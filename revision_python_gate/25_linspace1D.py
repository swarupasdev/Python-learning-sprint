from numpy import*
marks = linspace(1,8,5,endpoint = True)

#print(marks)

#without index
# for element in marks:
#         print(element)

#with index
n = len(marks)
for i in range(n):
    print("index",i,marks[i])