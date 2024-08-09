# Add a static method in problem 2, to greet the user with hello.
class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n*self.n}")

    def squareroot(self):
        print(f"The squareroot is {self.n** (1/2)}")
    def cube(self):
        print(f"The cube is {self.n*self.n*self.n}")

    @staticmethod
    def hello():
        print("Hello there!")

a = Calculator(int(input("Enter the number: ")))
a.hello()
a.square()
a.squareroot()
a.cube()

