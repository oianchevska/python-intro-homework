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
        #print (row)
   
# 4 filter to food
    food = [row for row in reader if row['category'] == 'Food']
    #print('-----------------------------------')
    #print (food)         
# Calculate the total amount spent on Food.
    total = 0
    now = datetime.now()
    print (f'Food Expense Report — generated {now.strftime("%B %d, %Y")}')
    for i in food:
        total += i['amount']
        print(f"{i['date']}: ${i['amount']}")
     
    
    print(f'Total: ${total}')
    
