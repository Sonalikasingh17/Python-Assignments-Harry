# Write a python function which converts inches to cms

def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter the number: "))    
                         
print(f"{n} inches in cms is:",inch_to_cms(n))
