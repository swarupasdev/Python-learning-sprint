#r is row & c is column
rows=int(input("Enter the rows: ")) 
for r in range(1,rows+1): #row jb tk chalega jitni i ki value hai
    for c in range(r):
        print(r,end=' ')
    print()
    
rows = int(input("Enter the rows: ")) 
for r in range(1, rows+1):
    for c in range(r):
        print('*', end=' ')
    print()