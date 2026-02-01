str1 = 'Hello Python'
print(str1)
#Using double quotes
str2 = "Hello Python"
print(str2)
#Using triple quotes
str3 ='''Triple quotes are generally used for
represent the multiline or
docstring'''
print(str3) 

'''#string indexing
str1 = 'Hello Python'
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])
print(str1[5])
print(str1[6])
print(str1[7])
print(str1[8])
print(str1[9])
print(str1[10])
print(str1[11])
print(str1[12])'''

#string slicing
str1 = 'Hello'
print(str1[0:4])
print(str1[0:1])
print(str1[1:3])
print(str1[0:2])
print(str1[0:3])
print(str1[0:4])

#string length #len() function
str1 = 'Hello Python'
print(len(str1))

#looping through string
str1 = 'Hello Python'
for i in str1:
    print(i)
    
#iterating through string #5ways
'''
#Using for loop
#Python range function
#Using the slice operator partially
#Traverse the string backward using the slice operator
#uBy using the indexing method
'''

#check string #in or not in
txt=" valentince day"
print("day" in txt)
print("day" not in txt)

#upper() method
txt="valentine day"
x=txt.upper()
print(x)

#lower() method
txt="VALENTINE DAY"
x=txt.lower()
print(x)

#strip() method
txt=" valentine day "
x=txt.strip()
print(x)

#replace() method
txt="valentine day"
x=txt.replace("day","night")
print(x)

#split() method
txt="valentine day"
x=txt.split()
print(x)

#concatenation
str1 = 'Hello'
str2 = 'Python'
print(str1 + str2)
print(str1*3)

#escape sequence
print("Hello\"Python\"")

#format() method: used to combine a string with the value inside the curly bracket
#format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are
#The format() method returns the formatted string
#The format() method formats the specified value(s) and insert them inside the string's placeholder.

print("Hello {}, your balance is {}.".format("Adam", 230.2346))
print("Hello {0}, your balance is {1}.".format ("Adam", 230.2346)) #positional argument  #0,1 are index #0 is Adam  and 1 is 230.2346 #index always start from 0 #index is used to avoid duplication #index is used to change the order of the string
print("Hello {name}, your balance is {blc}.".format(name="Adam", blc=230.2346)) #keyword argument

#format specifiers
i=7684919311
f=3.15
s="lakhs"
print("my no. is %d\nmy salary is %f in %s"%(i,f,s))