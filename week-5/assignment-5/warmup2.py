# Warmup 2: Input Validation with a While Loop

user_input = int(input("Enter a positive integer: "))

while user_input <= 0:
    try:
        print ("That's not a positive integer. Try again.")
        user_input = int(input("Enter a positive integer: "))
        if  user_input > 0:
            print(f"Got it: {user_input}")  
    except ValueError:
        print ("That's not a positive integer. Try again.")

