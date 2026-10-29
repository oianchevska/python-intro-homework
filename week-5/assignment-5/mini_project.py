
numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True:
    user_input = input("""
=== Number Cruncher ===
1. Find minimum
2. Find maximum
3. Search for a number
4. Sort the list
5. Quit
Choose an option (1-5): """)

    # Find minimum
    if user_input == "1":
        num_min = numbers[0]

        for num in numbers:
            if num < num_min:
                num_min = num

        print(f"Minimum number: {num_min}")

    # Find maximum
    elif user_input == "2":
        num_max = numbers[0]

        for num in numbers:
            if num > num_max:
                num_max = num

        print(f"Maximum number: {num_max}")

    # Search for a number
    elif user_input == "3":
        target = int(input("Please enter a number: "))
        found = False

        for i in range(len(numbers)):
            if numbers[i] == target:
                found = True
                break

        if found:
            print(f"Found {target} at index {i}.")
        else:
            print(f"{target} was not found in the list.")

    # Bubble Sort
    elif user_input == "4":
        swapped = True

        while swapped:
            swapped = False

            for i in range(len(numbers) - 1):
                if numbers[i] > numbers[i + 1]:
                    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                    swapped = True

        print(f"Sorted list: {numbers}")

    # Quit
    elif user_input == "5":
        print("Thanks for using Number Cruncher! See you next time!")
        break

    else:
        print("Invalid option. Please choose a number from 1 to 5.")
    