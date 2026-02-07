#common string method
#upper() returns string in upper case
mystr='hello swarup'
upper_case_mystr=mystr.upper()
print(upper_case_mystr)

#lower() returns string in lower case
lower_case_mystr=mystr.lower()
print(lower_case_mystr)

#strip() returns string with specified leading and trailing character removed . if no arguments is passed it removes leading and trailing whitespace
trim_mystr=mystr.strip('h')
print(trim_mystr)

#replace(old, new) returns string with all occurences old replaced by new
replaced_mystr=mystr.replace('hello', 'hey')
print(replaced_mystr)
