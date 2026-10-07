# Part 2: Mini-Project — Temperature Converter

temp_in_f = float(input("Enter a temperature in Fahrenheit: "))
temp_in_c = round(((temp_in_f - 32) * 5 / 9), 1)
print (f'{temp_in_f}°F is {temp_in_c}°C.')