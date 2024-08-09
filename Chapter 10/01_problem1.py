# Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
         self.name = name
         self.salary = salary
         self.pin = pin

p = Programmer("Sona", 120000, 600036)
print(p.name, p.salary, p.pin, p.company)
p = Programmer("Kashish", 125000, 800008)
print(p.name, p.salary, p.pin, p.company)
p = Programmer("Sapna", 140000, 605036)
print(p.name, p.salary, p.pin, p.company)
p = Programmer("Amrit", 150000, 403036)
print(p.name, p.salary, p.pin, p.company)
