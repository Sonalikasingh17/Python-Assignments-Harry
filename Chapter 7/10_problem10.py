# n = int(input("Enter the number: "))

# for i in range(1,11):
#     table =n*i
#     print(f"The multiplication table of {n} is",table)
#     print(f"The multiplication of {n} * {i} = {n*i}")

# Multiplication Table in Reverse Order
n = int(input("Enter the number: "))

for i in range(1,11):
    
    table = n*(11-i)
    print(f"The multiplication table of {n} * {11-i} is",table)