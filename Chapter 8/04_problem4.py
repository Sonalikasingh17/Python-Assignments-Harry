# Write a recursive function to calculate the sum of first n natural numbers.
''' 
sum(1) = 1
sum(2) = 1+2
sum(3) = 1+2+3

sum(n) = 1+2+3+4...+n
sum(n) = sum(n-1) + n
'''
def sum(n):
    if(n ==1):
        return 1
    return sum(n-1) + n

n = int(input("Enter the number: "))
print(f"Sum of {n} is:",sum(n))
