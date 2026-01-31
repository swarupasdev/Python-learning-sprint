
print("Armstrong Numbers in Range 1, 1000")
for i in range(1,1001):
    str_num = str(i)
    str_digit = len(str_num)

    sum = 0
    for j in str_num:
        sum += int(j) ** str_digit
    
    if(sum == i):
        print(i)
