# Write a program to calculate the factorial of a given number using for loop

n = int(input("Enter the number: "))

#i = 1 # No need to write this is extra line in the code
factorial = 1

for i in range(1,n+1):
    factorial *= i
    #i += 1 # No need

#print("The factorial of given number is:",factorial)
print(f"The factorial of {n} is {factorial}")


#using while loop
'''n = int(input("Enter the number: "))

i = 1 # No need to write this is extra line in the code
factorial = 1

while (i < n+1):
    factorial *= i
    i += 1

print(f"The factorial of {n} is {factorial}")
'''