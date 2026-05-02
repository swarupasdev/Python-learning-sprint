#common string methods
#split()split a string on a specified separator into a list of strings,if no string is specified it separates on white space
mystr="Hello San"
split_word=mystr.split()
print(split_word)

#join(iterable): joins elements of am iterable into a string with a separator
mylist=["Hello ", "San"]
newstring=''.join(mylist)
print(newstring)

#startswith(prefix): returns a boolean indicating if a string start with the specified prefix
start_with_hello=mystr.startswith('hello')
print(start_with_hello)

#endswith(suffix): returns a boolean if the string end s with a specific suffix 
end_with_san=mystr.endswith("San")
print(end_with_san)

#find(substring): returns the index of the 1st occurence of substring or -1 if it doesnot find one
world_index=mystr.find("San")
print(world_index)

#count(substring): returns the number of times a substring appears in a string
o_count=mystr.count('o')
print(o_count)

#capitalize(): returns a new string with the 1st character capitalized and the other characters lowercased
capitalized_mystr=mystr.capitalize()
print(capitalized_mystr)

#isupper(): returns true if all letters in the string are uppercase and false if not
is_upper=mystr.isupper()
print(is_upper)

#islower(): returns true if all letters in string are lowercase and false if not 
is_lower=mystr.islower()
print(is_lower)

#title(): returns a new string with capitalizing 1st letter of each word
is_capital=mystr.title()
print(is_capital)