# Read a Text File Line by Line
with open('C:/Users/19197/OneDrive/Documents/Code The Dream/python_class/python_homework/python-intro-homework/week-7/data/notes.txt', 'r') as file:
    for line in file:
        print(line.strip())