l1 = [10, 2, 25, 18, 9]
print("Original list:", l1)

# Sorting the list using nested loops (as you've done)

for i in range(0, len(l1)):
    for j in range(i + 1, len(l1)):
        if l1[i] >= l1[j]:
            l1[i], l1[j] = l1[j], l1[i]

print("Sorted list:", l1)

# Linear search for the value 9 in the sorted list
target = 9
found = False

for i in range(len(l1)):
    if l1[i] == target:
        found = True
        index = i
        break

if found:
    print(f"{target} found at index {index}")
else:
    print(f"{target} not found in the list")
