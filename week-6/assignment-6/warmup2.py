# Warmup 2: Functions that Return Values

def celsius_to_fahrenheit(c):
    result = (c * 9/5) + 32
    return round(result,1) 


def fahrenheit_to_celsius(f):
    result = (f - 32) * 5/9
    return round(result,1) 


print(f"0°C = {celsius_to_fahrenheit(0)}°F")
print(f"100°C = {celsius_to_fahrenheit(100)}°F")
print(f"72°F = {fahrenheit_to_celsius(99.8)}°C")
