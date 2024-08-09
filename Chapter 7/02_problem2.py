l = ["Harry", "Soham", "Sachin", "Rahul", "Monika", "Sonal", "Dipika", "Shubham"]

greet = input("Enter the greetings which you want to tell: ")

for name in l:
    if(name.startswith("S")):
      print(f"I am saying to {name}",greet, {name})

