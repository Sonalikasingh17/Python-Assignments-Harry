# Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from ‘Pets’.
#  Add a method ‘bark’ to class ‘Dog’.

class Animals:
    Animals = "Pets" #we can also skip this line. just write pass statement.

class Pets(Animals):
    Pets = "Dogs"    # we can also skip this line. just write pass statement.


class Dog(Pets):

    @staticmethod
    def bark():
        print("Bow Bow!")
         
d = Dog
d.bark()