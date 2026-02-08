#common string methods
#split()split a string on a specified separator into a list of strings,if no string is specified it separates on white space
mystr="Hello San"
split_word=mystr.split()
print(split_word)

#join(iterable): joins elements of am iterable into a string with a separator
mylist=["Hello ", "San"]
newword=''.join(mylist)
print(newword)