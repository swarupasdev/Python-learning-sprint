li = [1, 4, 5, 6, 7, 8]
sorted_list = li.sort()
left = 0
target = 10
right = len(li) - 1
while left <= right:
    mid = (right + left) // 2
    if li[mid] == target:
        print(mid)
        break
    elif li[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
if left > right:
    print("Element Didn't Exist")