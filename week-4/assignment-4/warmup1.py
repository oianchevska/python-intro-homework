# Warmup 1: List Operations

dog_breeds = dog_breeds = [
    "Basenji",
    "Corgi",
    "German Shepherd",
    "Collie",
    "Siberian Husky",
    "Akita",
    "Poodle",
    "Beagle"
]

# The first item

print(dog_breeds[0])

# The last item (use a negative index)
print(dog_breeds[-1])

# A slice containing only the middle four items
print(dog_breeds[2:6])

# The full list in reverse order

dog_breeds.reverse()
print(dog_breeds)
