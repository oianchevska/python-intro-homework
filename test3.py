# Part 2: Mini-Project — Refactor the Number Cruncher
numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

# find_min(numbers)
def find_min(n):
    num_min = n[0]

    for num in n:
        if num < num_min:
            num_min = num

    return (f"Minimum number: {num_min}")

# find_max(numbers)
def find_max(n):
    num_max = n[0]

    for num in n:
        if num > num_max:
            num_max = num

    return (f"Maximum number: {num_max}")

# Search for a number
def search (n, target):
    found = False
    index = -1
    for num in range(len(n)):
        if n[num] == target:
            found = True
            index = num
            break

    return (f"Found {target} at index {index}.")

# bubble_sort
def bubble_sort(n):
    swapped = True
    new_num = []
    for num in n:
        new_num.append(num)
    while swapped:
        swapped = False

        for num in range(len(new_num) - 1):
            if new_num[num] > new_num[num + 1]:
                new_num[num], new_num[num + 1] = new_num[num + 1], new_num[num]
                swapped = True
   
    return new_num

# show_menu
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

# main
def main():
    while True:
        user_input = int(show_menu())
       
        if user_input not in (1,2,3,4,5):
            print ("Please select from 1-5")

        # Find minimum
        elif user_input == 1:
            print(find_min(numbers))

        # Find maximum
        elif user_input == 2:
            print(find_max(numbers))

        # Search for a number
        elif user_input == 3:
            target = int(input("Please enter a number: "))
            print (search(numbers, target))

        # Bubble Sort
        elif user_input == 4:           
            print(bubble_sort(numbers))

        # Quit
        elif user_input == 5:
            print("Thanks for using Number Cruncher! See you next time!")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 5.")
        
main()
