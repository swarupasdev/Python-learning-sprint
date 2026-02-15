#local scope(l): Variables defined in functions or classes.

def my_func():
    my_var=10
    print(my_var)
my_func()
#print(my_var) NAMEERROR
def outer_func():
    msg='Hello There!'
    def inner_func():
        print((msg))
        
        inner_func()
outer_func
#enclosing scope(E): Variables defined in enclosing or nested functions.

#Global scope(G): Variables defined at the top level of the module or file.
#Built-in scope(B): Reserved names in Python for predefined functions, modules, keywords, and objects.
