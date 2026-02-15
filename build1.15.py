#reusable piece of code that run when you call them
#input()
name=input("What is your name? ans:")
print('Hello', name)

#int()
print(int(3.14))
print(int('42'))
print(int(True))
print(int(False))

#def functionname():
def eat():
    eaten=input("What did you have for the lunch? ans:")
    print(eaten, " is very refreshing.")
eat()

def calc_sum(a,b):
    print(a+b)
calc_sum(3,4)
calc_sum(89,23)

def calc_mult(x,y):
    return x*y

my_mult=calc_mult(2,5)
print(my_mult)