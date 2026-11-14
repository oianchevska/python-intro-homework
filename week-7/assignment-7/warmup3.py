# Warmup 3: Use the os Module
import os
print(f'{os.getcwd()}')  # e.g., /Users/yourname/projects

if os.path.exists("python-intro-homework/week-7/data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

file_path = os.path.join("python-intro-homework","week-7","data", "expenses.csv")
print(file_path) 


