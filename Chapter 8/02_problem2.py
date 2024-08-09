# Write a python program using function to convert Celsius to Fahrenheit.

'''c = int(input("Enter the temperature in celsius: "))

convert = ((9/5)* c) + 32

print(f"The temperature in farenheit is {convert} F")

'''

# Using function
def c_to_f(c):
    return ((9/5)*c) + 32

c = int(input("Enter the temperature in celsius: "))
x = c_to_f(c)
print(f"{round(x,2)} F")


# Chatgpt Suggestion
# Function to convert Celsius to Fahrenheit
def c_to_f(c):
    return (9/5) * c + 32

# Taking user input for Celsius temperature
try:
    c = float(input("Enter the temperature in Celsius: "))
    x = c_to_f(c)
    print(f"{round(x, 2)} °F")
except ValueError:
    print("Please enter a valid number.")


