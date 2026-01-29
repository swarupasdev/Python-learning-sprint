def doubler(x):
    return x*2
l=[1,2,3,4,5,6]

mod_list=map(doubler,l)
print(list(mod_list))

#double each value with 2
l=[1,2,3,4,5,6]
doubler=map(lambda x:x*2,l)
print(list(doubler))

#output: [2, 4, 6, 8, 10, 12]