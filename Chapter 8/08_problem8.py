# Write a python function to print multiplication table of a given number.

def multiply(n):
    for i in range(1, 11):
        print(f"{n}*{i} = {n*i}")
        

n = int(input("Enter the number: "))
multiply(n)


# Chatgpt Suggestion
# Function to print the multiplication table of a given number
'''
def multiply(n):
    print(f"The multiplication table of {n} is:")
    for i in range(1, 11):
        print(f"{n} * {i} = {n * i}")

# Taking user input for the number
try:
    n = int(input("Enter the number: "))
    multiply(n)
except ValueError:
    print("Please enter a valid integer.")
    '''

