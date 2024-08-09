
marks1 = int(input("Enter the marks of math : "))
marks2 = int(input("Enter the marks of science: "))
marks3 = int(input("Enter the marks of english: "))

#Check for total percentage
total_percentage = ((marks1 + marks2 + marks3)*100)/300

if (total_percentage >= 40 and marks1>=33 and marks1>=33 and marks1>=33):
    print("You are passed, Congrats!\nYour total_percentage is:",total_percentage)

else:
    print("You failed, try again next year!\nYour total_percentage is:",total_percentage)

#Check subject wise percentage
percentage1 = (marks1 * 100)/100
percentage2 = (marks2 * 100)/100
percentage3 = (marks3 * 100)/100


if (percentage1 >= 33):
    print("You are passed in math with percentage of:",percentage1)
else:
    print("You failed in math")

if (percentage2 >= 33):
    print("You are passed in science with percentage of:",percentage2)
else:
    print("You failed in science ")

if (percentage3 >= 33):
    print("You are passed in english with percentage of:",percentage3)
else:
    print("You failed in english")
   



