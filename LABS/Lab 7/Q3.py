students = [
    {"name": "John", "age": 17},
    {"name": "Emma", "age": 19},
    {"name": "Sam", "age": 20},
    {"name": "Kelly", "age": 16}
]

# Sort by name
sorted_by_name = sorted(students, key=lambda x: x['name'])

# Sort by age
sorted_by_age = sorted(students, key=lambda x: x['age'])

print("Sorted by name:", sorted_by_name)
print("Sorted by age:", sorted_by_age)