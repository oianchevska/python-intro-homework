
age = input("Enter your age: ")
next_year = age + 1
print(next_year)

# Error message:
# TypeError: can only concatenate str (not "int") to str

# Cause:
# input() returns a string, but I tried to add an integer to it.

# Fix:
age = int(input("Enter your age: "))
next_year = age + 1

print(f"Next year you will be {next_year} years old.")