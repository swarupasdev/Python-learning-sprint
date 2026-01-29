# Convert from one data type to another

# Example 1: Convert a string to an integer
string_num = "42"
integer_num = int(string_num)
print("String to Integer:", integer_num)

# Example 2: Convert an integer to a float
int_num = 42
float_num = float(int_num)
print("Integer to Float:", float_num)

# Example 3: Convert a float to an integer (truncates decimal part)
float_num = 3.14159
int_num = int(float_num)
print("Float to Integer:", int_num)

# Example 4: Convert an integer to a string
integer_num = 42
string_num = str(integer_num)
print("Integer to String:", string_num)

# Example 5: Convert a string to a list of characters
string = "Hello"
char_list = list(string)
print("String to List of Characters:", char_list)

# Example 6: Convert a list of integers to a set
integer_list = [1, 2, 3, 3, 4, 5]
integer_set = set(integer_list)
print("List to Set:", integer_set)
