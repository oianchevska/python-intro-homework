# Warmup 4: Validation Function

user_input = int(input("Please enter the number: "))

def is_valid_score(score):
    if score < 0 or score > 100:
        return False
    else:
        return True


if is_valid_score(user_input) == True:
    print("Valid score.")
else:
    print("Invalid score — must be between 0 and 100.")