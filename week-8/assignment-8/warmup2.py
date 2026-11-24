# Warmup 2: Safe Division
try:
    user_input1 = int(input('Enter the numerator: '))
    user_input2 = int(input('Enter the denominator: '))
    result = user_input1 / user_input2
    print(f'{user_input1} ÷ {user_input2} = {result}')

except ZeroDivisionError:
    print("You can't divide by zero.")