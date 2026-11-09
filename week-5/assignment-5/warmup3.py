# Warmup 3: Linear Search
names = ["vera", "sasha", "artur", "alla","stesha"]
target = input ("Enter a name to search for: ").lower()


def name_search (data,target):
    found = False
    index = -1
    for i in range(len(names)):
        if names[i] == target:
            found = True
            index = i
        

    if found:
        print (f"Found {target.capitalize()} at index {index}.")
    else:
        print(f"{target.capitalize()} was not found in the list.")

name_search(names,target)