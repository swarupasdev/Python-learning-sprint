#a+b=c, where there are two operands and a plus (+) operator, and the result turns c.

#1. #arithmetic operators
print(2+3) #addition
print(2-3) #subtraction
print(2*3) #multiplication
print(2/3) #division
print(2%3) #modulus
print(2**3)#exponentiation
print(2//3)#floor division

#2. #assignment operators
x=5
print(x) #assigns 5 to x
x+=3
print(x) #adds 3 to x
x-=3
print(x) #subtracts 3 from x
x*=3
print(x) #multiplies 3 to x
x/=3
print(x) #divides 3 from x
x%=3
print(x) #modulus 3 from x
x**=3
print(x) #exponentiation 3 from x
x//=3
print(x) #floor division 3 from x

#3. #comparison operators
x=5
y=3
print(x==y) #equal to
print(x!=y) #not equal to
print(x>y) #greater than
print(x<y) #less than
print(x>=y) #greater than or equal to
print(x<=y) #less than or equal to

#4. #logical operators
x=5
print(x>3 and x<10) #and true if both statements are true
print(x>3 or x<4) #or true if one of the statements is true
print(not(x>3 and x<10)) #not reverse the result, returns false if the result is true
print(not(x>3 or x<4)) #not reverse the result, returns false if the result is true

#5. #identity operators
x=["apple","banana"] #square brackets are used for lists
y=["apple","banana"]
z=x #z is the same object as x
print(x is z) #is true if both variables are the same object
print(x is y) #is false because x is not the same object as y, even if they have the same content
print(x==y) #to demonstrate the difference between "is" and "==": this comparison returns true because x is equal to y
print(x is not z) #is false because z is the same object as x
print(x is not y) #is true because x is not the same object as y, even if they have the same content
print(x!=y) #to demonstrate the difference between "is not" and "!=": this comparison returns false because x is equal to y

x1=5.0
if(type(x1) is int):
    print("true")
else:
 print("false")
 
#6. #membership operators
x=["apple","banana"]
print("banana" in x) #in returns true if a sequence with the specified value is present in the object
print("pineapple" not in x) #not in returns true if a sequence with the specified value is not present in the object

#7. #bitwise operators
#bitwise operators are used to compare (binary) numbers
#bitwise operators work on binary numbers
#bitwise operators are used to perform bitwise calculations
#bitwise operators work on bits and perform bit by bit operation
#assume if a=60 and b=13
#in binary format they will be as follows:
#a=0011 1100
#b=0000 1101
#a&b=0000 1100
#a|b=0011 1101
#a^b=0011 0001
#~a=1100 0011
#a<<2=1111 0000
#a>>2=0000 1111
a=60
b=13
print(a&b) #and sets each bit to 1 if both bits are 1
print(a|b) #or sets each bit to 1 if one of two bits is 1
print(a^b) #xor sets each bit to 1 if only one of two bits is 1
print(~a) #not inverts all the bits
print(a<<2) #zero fill left shift shifts left by pushing zeros in from the right and let the leftmost bits fall off
print(a>>2) #signed right shift shifts right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

#8. #operator precedence
#operator precedence determines the grouping of terms in an expression
#this affects how an expression is evaluated
#consider the expression 5+2*3
#multiplication has a higher precedence than addition, so the above expression is equivalent to 5+(2*3) = 11
#here, parentheses can be used to force the priority
#so, (5+2)*3 = 21
#the following table lists the operators in order of precedence, from highest to lowest
#operator: description
#** : exponentiation
#~ + - : complement, unary plus and minus (method names for the last two are +@ and -@)
#* / % // : multiply, divide, modulo and floor division
#+ - : addition and subtraction
#>> << : right and left bitwise shift
#& : bitwise 'and'
#^ | : bitwise exclusive 'or' and regular 'or'
#<= < > >= : comparison operators
#<> == != : equality operators
#= %= /= //= -= += *= **= : assignment operators
#is is not : identity operators
#in not in : membership operators
#not or and : logical operators
#example: 2+3*4
#here, 3*4=12 and 2+12=14
#example: 2+3*4**2
#here, 4**2=16, 3*16=48, 2+48=50
#example: 2+3*4**2/10
#here, 4**2=16, 3*16=48, 48/10=4.8, 2+4.8=6.8
#example: (2+3)*4**2/10
#here, 2+3=5, 4**2=16, 5*16=80, 80/10=8.0
#example: (2+3)*4**(2/10)
#here, 2+3=5, 2/10=0.2, 4**0.2=1.3195079107728942, 5*1.3195079107728942=6.597539553864471, 6.597539553864471
#example: 2**3**2
#here, 3**2=9, 2**9=512
#example: 2**(3**2)
#here, 3**2=9, 2**9=512
#example: (2**3)**2
#here, 2**3=8, 8**2=64
#example: 2*(3+4)
#here, 3+4=7, 2*7=14
#example: 2*(3+4)**2
#here, 3+4=7, 7**2=49, 2*49=98
#example: 2*(3+4)**2/2
#here, 3+4=7, 7**2=49, 2*49=98, 98/2=49.0
#example: 2*(3+4)**2//2
#here, 3+4=7, 7**2=49, 2*49=98, 98//2=49
#example: 2*(3+4)**2//2**2
#here, 3+4=7, 7**2=49, 2*49=98, 2**2=4, 98//4=24
#example: 2*(3+4)**2//2**2-1
#here, 3+4=7, 7**2=49, 2*49=98, 2**2=4, 98//4=24, 24-1=23
#example: 2*(3+4)**2//2**2-1+2
#here, 3+4=7, 7**2=49, 2*49=98, 2**2=4, 98//4=24, 24-1=23, 23+2=25
#example: 2*(3+4)**2//2**2-1+2/2
#here, 3+4=7, 7**2=49, 2*49=98, 2**2=4, 98//4=24, 24-1=23, 2/2=1.0, 23+1.0=24.0
#example: 2*(3+4)**2//2**2-1+2//2
#here, 3+4=7, 7**2=49, 2*49=98, 2**2=4, 98//4=24, 24-1=23, 2//2=1, 23+1=24

#9. #ternary operator
#ternary operators also known as conditional expressions are operators that evaluate something based on a condition being true or false
#it was added to python in version 2.5
#it simply allows to test a condition in a single line replacing the multiline if-else making the code compact
#syntax: [on_true] if [expression] else [on_false]
#example: x=5
#y=10
#print("x is greater than y") if x>y else print("x is less than or equal to y")
#example: x=5
#y=10
#print(x) if x>y else print(y)
#example: x=5
#y=10
#print("x is greater than y") if x>y else print("=") if x==y else print("x is less than y")
#example: x=5
#y=10
#print("x is greater than y") if x>y else print("=") if x==y else print("x is less than y")

#10. #special operators
#python language offers some special type of operators like the identity operator or the membership operator
#membership operators
#in and not in are the membership operators in python
#they are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary)
#in: true if value/variable is found in the sequence
#not in: true if value/variable is not found in the sequence
#example: x="hello world"
#print("h" in x)
#example: x="hello world"
#print("hello" in x)
#example: x="hello world"
#print("hello" not in x)
#example: x=[1,2,3,4,5]
#print(1 in x)
#example: x=[1,2,3,4,5]
#print(6 in x)
#example: x=[1,2,3,4,5]
#print(1 not in x)
#example: x=[1,2,3,4,5]
#print(6 not in x)

#11. #keywords
#keywords are the reserved words in python
#we cannot use a keyword as a variable name, function name or any other identifier
#keywords are case sensitive
#there are 33 keywords in python 3.7.0
#all the keywords except True, False and None are in lowercase and they must be written as they are
#the list of all the keywords are given below
#False: it represents the boolean false
#None: it represents the null object
#True: it represents the boolean true
#and: it is a logical operator
#as: it is used to create an alias
#assert: it is used for debugging
#async: it is used to define a coroutinejn[]
#await: it is used to pause the execution of the coroutine
#break: it is used to break out of a loop
#class: it is used to define a class
#continue: it is used to continue to the next iteration of a loop
#def: it is used to define a function
#del: it is used to delete an object
#elif: it is used in conditional statements, same as else if
#else: it is used in conditional statements
#except: it is used with exceptions, what to do when an exception occurs
#finally: it is used with exceptions, a block of code that will be executed no matter if there is an exception or not
#for: it is used to create a for loop
#from: it is used to import specific parts of a module
#global: it is used to declare a global variable
#if: it is used to make a conditional statement
#import: it is used to import a module
#in: it is used to check if a value is present in a list, tuple, etc.
#is: it is used to test if two variables are equal
#lambda: it is used to create an anonymous function
#nonlocal: it is used to declare a non-local variable
#not: it is a logical operator
#or: it is a logical operator
#pass: it is a null statement, it is used when a statement is required syntactically but you do not want any command or code to execute
#raise: it is used to raise an exception
#return: it is used to exit a function and return a value
#try: it is used to make a try...except statement
#while: it is used to create a while loop
#with: it is used to simplify exception handling
#yield: it is used to end a function and return a generator


  