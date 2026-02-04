#multiple  strings combined with each other is concatination
mystr1='I am'
mystr2='San'
str_conc1=mystr1+' '+mystr2
print(str_conc1,'\n')
# str() anthting inside it can convert the subject to string
mystr3='My age is'
mynum=23
str_conc2=mystr3+' '+str(mynum)
print(str_conc2,'\n')
#string interpolation
#process of inserting variables and other expressions in to a string 
#keep it inside the {}
work='Yobytech'
time=3
full_str=f'I am working in {work} since {time} years'
#f is formatted string literal
print(full_str)