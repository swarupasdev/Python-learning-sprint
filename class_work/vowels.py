v=input("Find the vowels")
list1=['a','e','i','o','u']
list2=['A','E','I','O','U']
count=0
for char in range(v.len):
    if char==list1 or char==list2:
        print(char)
        count+=count