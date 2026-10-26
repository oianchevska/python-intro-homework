# Warmup 3: Set Operations

# Create two hardcoded lists of programming languages (some overlap, some unique to each list). Convert each to a set and print:
list_1 = ["Python", "Java", "SQL", "C++","Go"]
list_2 = ["PHP","Python", "JavaScript", "SQL", "Ruby"]

set_1 = set(list_1)
set_2 = set(list_2)

print (set_1)
print(set_2)

# The union (all languages from both lists, no duplicates)
print(set_1.union(set_2))

# The intersection (languages in both lists)
print(set_1.intersection(set_2))

# The difference (languages only in the first list)

print(set_1.difference(set_2))