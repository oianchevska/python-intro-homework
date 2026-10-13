# Part 2: Mini-Project — Day Planner

day = input("What day is it? ").strip().capitalize()
time = input("What time of day? ").strip().lower()

if day not in ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"):
    print("Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday...")
else:

    if day == 'Monday':
        if time == 'morning':
            print(f'Suggestion: {day} {time} is a great time to plan and organize tasks for the week ahead.')
        elif time == 'afternoon':
            print(f'Suggestion: {day} {time} is a great time to take a small break.')
        elif time == 'evening':
            print(f"Suggestion: {day} {time} - Don't forget to feed the cat!") 

    elif day == 'Tuesday':
        if time == 'morning':
            print(f'Suggestion: {day} {time} Python class — great time to focus!')
        elif time == 'afternoon':
            print(f'Suggestion: {day} {time} is a great time for a cup of tea!')
        elif time == 'evening':
            print(f"Suggestion: {day} {time} - Go to the gym and unwind after a busy day!") 

    elif day == 'Friday':
        if time == 'morning':
            print(f'Suggestion: {day} {time} think about the weeekend plans, it is the last day of the workweek!')
        elif time == 'afternoon':
            print(f'Suggestion: {day} {time} is a great time for a cup of coffe!')
        elif time == 'evening':
            print(f"Suggestion: {day} {time} - Check what's playing at the movie theater and enjoy some time to relax!") 

    elif day == 'Saturday':
        if time == 'morning':
            print(f'Suggestion: {day} {time} - Stay in bed and relax. You deserve some rest!')
        elif time == 'afternoon':
            print(f'Suggestion: {day} {time} - Take your dog for a walk and enjoy the sunshine!')
        elif time == 'evening':
            print(f"Suggestion: {day} {time} It's a great time to try a new local restaurant!") 

