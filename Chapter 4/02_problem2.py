students_marks =  []

s1 = int(input("Enter student marks: "))  #here we can change all occurences by selecting which we have to changeand also for change in end press end and finish it.
students_marks.append(s1)
s2 = int(input("Enter student marks: "))
students_marks.append(s2)
s3 = int(input("Enter student marks: "))
students_marks.append(s3)
s4 = int(input("Enter student marks: "))
students_marks.append(s4)
s5 = int(input("Enter student marks: "))
students_marks.append(s5)
s6 = int(input("Enter student marks: "))
students_marks.append(s6)

students_marks.sort()

print(students_marks)



# Chatgpt Suggestions

# Initialize an empty list to store marks
students_marks = []

# Loop to accept marks from 6 students
for i in range(6):
    mark = int(input(f"Enter marks for student {i+1}: "))
    students_marks.append(mark)

# Sort the list of marks
students_marks.sort()

# Print the sorted marks
print("Sorted marks:", students_marks)


# Updated Chatgpt Suggestion
#This code also validate our marks 
# Initialize an empty list to store marks
students_marks = []

# Function to validate marks within the range of 0 to 100
def validate_marks(mark):
    return 0 <= mark <= 100

# Loop to accept marks from 6 students
for i in range(6):
    while True:
        try:
            mark = int(input(f"Enter marks for student {i+1}: "))
            if validate_marks(mark):
                students_marks.append(mark)
                break  # Exit the loop if mark is valid
            else:
                print("Error: Marks should be between 0 and 100.")
        except ValueError:
            print("Error: Enter a valid integer for marks.")

# Sort the list of marks
students_marks.sort()

# Print the sorted marks
print("Sorted marks:", students_marks)
