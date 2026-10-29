# Warmup 2: Input Validation with a While Loop

while True:
    try:
        user_input = int(input("Enter a positive integer: "))

        print ("That's not a positive integer. Try again.")
        if  user_input > 0:
            print(f"Got it: {user_input}")  
        else:
            print ("That's not a positive integer. Try again.")   
    except ValueError:
        print ("That's not a positive integer. Try again.")

