n = []
n1 = int(input("Enter the 1st number: "))
n.append(n1)
n2 = int(input("Enter the 2nd number: "))
n.append(n2)
n3 = int(input("Enter the 3rd number: "))
n.append(n3)
n4 = int(input("Enter the 4th number: "))
n.append(n4)

print(n)
print("Greatest number is ",max(n))

# Code with Harry
a1 = int(input("Enter the number 1: "))
a2 = int(input("Enter the number 2: "))
a3 = int(input("Enter the number 3: "))
a4 = int(input("Enter the number 4: "))

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number is a1:", a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number is a2:", a2)

elif(a3>a1 and a3>a2 and a3>a4):
    print("Greatest number is a3:", a3)

elif(a4>a1 and a4>a2 and a4>a3):
    print("Greatest number is a4:", a4)

