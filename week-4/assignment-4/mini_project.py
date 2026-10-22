students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

# Find the top scorer
max_score =  students[0]["score"]
name = []
for student in students:
    if max_score < student["score"]:
        max_score= student["score"]
        name = student["name"]
print (f"Top scorer:  {name} ({(max_score)})")

# Calculate the class average
total = 0
for student in students:
    total += student["score"]
average = total / len(students)
print(f"Class average: {average}")

# List all unique subjects
list_subject = []
for student in students:
    list_subject.append(student["subject"])
set_subject =  set(list_subject )
print(f"Subjects offered: {set_subject}")

# List high scorers 

high_scores_students =[]
for student in students: 
    if student["score"] >75:
         high_scores_students.append(student["name"])    
print(f"High scorers: {high_scores_students}")