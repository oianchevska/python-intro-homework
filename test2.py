# Part 2: Mini-Project — Refactor the Number Cruncher
numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

def show_menu():
     
    user_input = input("""
        === Number Cruncher ===
        1. Find minimum
        2. Find maximum
        3. Search for a number
        4. Sort the list
        5. Quit
        Choose an option (1-5): """)

    return user_input

print(show_menu())