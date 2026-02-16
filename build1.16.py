#local scope(l): Variables defined in functions or classes.

def my_func():
    my_var=10
    print(my_var)
my_func()
#print(my_var) NAMEERROR

#enclosing scope(E): Variables defined in enclosing or nested functions.
def outer_func():
    msg='Hello There!'
    def inner_func():
        print((msg))
        
    inner_func()
outer_func()
#outer function is accesing the inner function
def outer_func():
    msg = 'Hello there!'
    res = ""  # Declare res in the enclosing scope

    def inner_func():
        nonlocal res  # Allow modification of an enclosing variable
        res = 'How are you?'
        print(msg)  # Accessing msg from outer_func()
    inner_func()
    print(res)  # Now res is accessible and modified
outer_func()

# Output:
# Hello there!
# How are you?

#Global scope(G): Variables defined at the top level of the module or file.
my_var1=10

def show_var():
    print(my_var1)
show_var()
#print(my_var1)

my_var2=7
def show_vars():
    global my_var3
    my_var3=17
    print(my_var2)
    print(my_var3)
show_vars()
print(my_var3)

my_var = 10  # A global variable

def change_var():
    global my_var  # Allows modification of a global variable
    my_var = 20

change_var()
print(my_var)  # my_var is now modified globally to 20

#Built-in scope(B): Reserved names in Python for predefined functions, modules, keywords, and objects.


