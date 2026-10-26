# Warmup 2: Dictionary Operations

students =  {"name": "Oleksandra", "grade": 10, "subjects": ["Math", "English", "Art"]}

# Print each key-value pair using .items() in a for loop

for key, value in students.items():
    print(f"{key}: {value}")

# Add a new key "graduated" with the value False
students["graduated"]= False

# Print the updated dictionary
print(students)
