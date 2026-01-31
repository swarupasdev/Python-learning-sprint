def get_user_input():
    try:
        num_entries = int(input("How many pairs of name and age do you want to add? "))
        user_data = {}

        for _ in range(num_entries):
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            user_data[name] = age

        return user_data
    except ValueError:
        print("Invalid input! Please enter a number.")
        return {}

# Utility functions
def add_pair(name, age, dictionary):
    dictionary[name] = age

def delete_pair(name, dictionary):
    if name in dictionary:
        del dictionary[name]
    else:
        print(f"{name} not found in the dictionary.")

def update_age(name, new_age, dictionary):
    if name in dictionary:
        dictionary[name] = new_age
    else:
        print(f"{name} not found in the dictionary.")

def count_pairs(dictionary):
    return len(dictionary)

def get_age(name, dictionary):
    return dictionary.get(name, f"{name} not found in the dictionary.")

def clone_dict(dictionary):
    cloned_dict = dictionary.copy()
    return id(dictionary), id(cloned_dict)

def lists_to_dict(names, ages):
    return dict(zip(names, ages))

def string_to_dict(input_string):
    try:
        result_dict = eval(input_string)
        if isinstance(result_dict, dict):
            return result_dict
        else:
            return "Input string does not represent a dictionary."
    except Exception as e:
        return f"Error: {e}"


data = get_user_input()
print("You entered the following data:")
for name, age in data.items():
    print(f"{name}: {age} years")

print()
print("Add users Information using Function")
add_pair("Harshit",15,data)
add_pair("Anurag",25,data)
for name, age in data.items():
    print(f"{name}: {age} years")

print()
print("Delete Information: ")
delete_pair("Harshit",data)
for name, age in data.items():
    print(f"{name}: {age} years")

print()
print("Update the Age: ")
update_age("Anurag",20,data)
for name, age in data.items():
    print(f"{name}: {age} years")

print()
print("Count the Number of Pair in Dictionary:")
print(count_pairs(data))
print()
print("Get the Age Using Function: ")
print(get_age("Anurag",data))
print()
print("Clone the Dictinary")
print(clone_dict(data))
print()
print("List to dictionary: ")
names = ["Sachin","Garuna"]
Ages = [15,25]
lists_to_dict(names,Ages)
for name, age in data.items():
    print(f"{name}: {age} years")

print()
print("String to dictionary: ")
input_str = "{'name': 'John', 'age': 30}"
output = string_to_dict(input_str)
print(output)



