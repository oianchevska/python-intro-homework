# Warmup 3: Scope in Action

def show_name():
    name = "Hello My name is Sasha"
    print(name)

# show_name()

# print(name)

# ERROR: NameError: name 'name' is not defined

def show_name():
    name = "Hello My name is Sasha"
    return name

result = show_name()
print(result)