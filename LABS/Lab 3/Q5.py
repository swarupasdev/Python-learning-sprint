String = str(input("Enter the String: "))
lower_String = String.lower()

alphabet_count = {}

for char in lower_String:
    if char.isalpha():
        if char in alphabet_count:
            alphabet_count[char] += 1
        else:
            alphabet_count[char] = 1

for alphabet, count in alphabet_count.items():
    print(f"{alphabet}: {count}")
