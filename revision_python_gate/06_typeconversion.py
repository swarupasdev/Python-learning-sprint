#implicit type conversion
a1 = 5
b1 = 1
value1 = 5/1

# to know the datatype of an expression type() method
print(value1)
print(type(value1))

a2 = 10
b2 = 5.5
total2 = a2 + b2
print(total2)
print(type(total2))

a3 = "hey"
b3 = "Swarup"
print(a3+b3)  # in case of string this is called string concatenation
print(type(a3+b3))

a4 = 10
b4 = '5.5'
#total4 = a4 + b4
#print(total4)
# you can't concatenate this in implicit type : typeerror unsupported operand

#explicit type conversion
a5 = 5
b5 = 2
value5 = a5 / b5
int_value5 = int(value5)
print(value5)
print(type(int_value5))

a6 = 10
b6 = '5.5'
total6 = a6 + float(b6)

print(total6)
print(type(total6))

a7 = 69
b7 = "Swarup"
total7=a7+int(b7)
print(total7)
print(type(total7))   #you can not convert this  


