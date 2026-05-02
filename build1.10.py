#numbers and mathematical operations
#floor ivision (//)
myint1=5
myint2=4
myfloat1=4.623
myfloat2=5.0
myfloordiv1=myint1//myint2
myfloordiv2=myfloat1//myfloat2
print('Integer floor division:',myfloordiv1)
print('Float floor division:',myfloordiv2)

#exponentiation (**)
expint=myint1**myint2
expfloat=myfloat1**myfloat2
print('Int exponentiation:',expint)
print('Float exponentiation:',expfloat)

#conversion float to int and vice versa
myfloat3=float(myint1)
print(myfloat3)

myint3=int(myfloat2)
print(myint3)

mystrint='45'
mystrfloat='5.6'
new_int=int(mystrint)
new_float=float(mystrfloat)
print(mystrint)
print(mystrfloat)

#round(): rounds a number to a specified number of decimcal places. by default this function rounds to the nearest integer and returns a whole number woth no decimal places
rounded_int=round(myfloat1)
print(rounded_int)

#abs(): returns the absolute value of a number
num= -15
absolute_value=abs(num)
print(absolute_value)

#pow(): raises a number to the power of another or performs modular exponentiation.
sum1=pow(4,5)
print(sum1)

sum2=pow(3,6,2)
print(sum2)
