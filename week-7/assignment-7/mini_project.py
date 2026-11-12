# Expense Report Generator
import os
from datetime import datetime
import csv

# 1 Use os.path.exists() to verify that file exists 
if os.path.exists("python-intro-homework/week-7/data/expenses.csv"):
    pass
else:
    print("File not found.")

# 2 Read the file into a list of dictionaries using csv.DictReader.    
with open('C:/Users/19197/OneDrive/Documents/Code The Dream/python_class/python_homework/python-intro-homework/week-7/data/expenses.csv', 'r') as file:
#with open('../expenses.csv', 'r') as file:   
    reader = list(csv.DictReader(file))
    for row in reader:
        row['amount'] = float(row['amount'])
   
# 4 filter to food
    food = [row for row in reader if row['category'] == 'Food']
         
# Calculate the total amount spent on Food.
    with open('C:/Users/19197/OneDrive/Documents/Code The Dream/python_class/python_homework/python-intro-homework/week-7/data/food_report.txt', 'w') as file:
        total = 0
        now = datetime.now()
        file.write (f'Food Expense Report — generated {now.strftime("%B %d, %Y")}\n')
        for i in food:
            total += i['amount']
            file.write(f"{i['date']}: ${i['amount']:.2f}\n") 
        file.write(f'Total: ${total:.2f}')