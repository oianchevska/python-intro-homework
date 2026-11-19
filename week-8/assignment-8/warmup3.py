# Warmup 3: Handle a Missing File
try:
    with open('C:/Users/19197/OneDrive/Documents/Code The Dream/python_class/python_homework/python-intro-homework/week-8/data/missing.txt', 'r') as file:
        content = file.read()
    print("File read successfully.")
except FileNotFoundError:
    print("Error: missing.txt was not found. Please check the file path and try again.")
