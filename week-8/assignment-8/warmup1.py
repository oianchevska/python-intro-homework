# Warmup 1: Validate Numeric Input
while True: 
    try:
        user_input = float(input('Enter a number: '))
        print(user_input)
        break

    except ValueError :
        print("That's not a valid number. Try again.")       
