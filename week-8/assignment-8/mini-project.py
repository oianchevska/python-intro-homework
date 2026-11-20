import csv 

try:
    with open('C:/Users/19197/OneDrive/Documents/Code The Dream/python_class/python_homework/python-intro-homework/week-8/data/messy_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        rows_attempted = 0
        skipped_rows = 0
        clean_data = []
    

        for row_number, row in enumerate(reader, start=1):
            rows_attempted += 1

            if None in row:
                print(f"Row {row_number}: extra column detected — skipped")
                skipped_rows += 1
                continue

            try:
                row['amount'] = float(row['amount'])
                clean_data.append(row)

            except (ValueError, KeyError) as e:
                skipped_rows += 1
                print(f"Row {row_number}: {type(e).__name__}: {e}")
                #print(f"Skipping invalid row {row_number}")
                continue

 

except FileNotFoundError:
    print("Error: missing.txt was not found. Please check the file path and try again.")

rows_parsed = rows_attempted - skipped_rows
# report
print("=== CSV Report ===")
print(f'Rows attempted: {rows_attempted}')
print(f'Rows parsed: {rows_parsed}')
print(f'Rows skipped: {skipped_rows}')    
#print(f'{name_data} | {category_data}| {amount_data}')
print("Clean data:")

for item in clean_data:
    print(f"{item['name']} | {item['category']} | ${item['amount']:.2f}")