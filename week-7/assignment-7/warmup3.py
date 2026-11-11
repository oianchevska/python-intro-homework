# Warmup 3: Use the os Module
import os
print(f'YOU ARE HERE: {os.getcwd()}')  # e.g., /Users/yourname/projects
if os.path.exists("python-intro-homework/week-7/data/expenses.csv"):
    print("Found it!")
else:
    print("File not found.")

file_path = os.path.join("python-intro-homework","week-7","data", "expenses.csv")
print(file_path)   


print(os.path.exists(file_path)) 


