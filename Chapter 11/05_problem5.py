# Write a class vector representing a vector of n dimensions.
# Overload the + and * operator which calculates the sum and the dot(.) product of them.

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    
    def __mul__(self, other):
        result = (self.x * other.x+ self.y * other.y+ self.z * other.z )
        return result
    
    def __str__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"
    
#Test the implementation
v1 = Vector(2, 3, 4)
v2 = Vector(5, 6, 7)
v3 = Vector(1, 8, 4)

print(v1 + v2)
print(v1 * v2)

print(v1 + v3)
print(v1 * v3)

print(v2 + v3)
print(v2 * v3)

'''
class Vector:
    def __init__(self, *components):
        self.components = components

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension to add.")
        added_components = [a + b for a, b in zip(self.components, other.components)]
        return Vector(*added_components)

    def __mul__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension to calculate dot product.")
        dot_product = sum(a * b for a, b in zip(self.components, other.components))
        return dot_product

    def __str__(self):
        return f"Vector({', '.join(map(str, self.components))})"

# Example usage
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1 + v2)  # Output should be Vector(5, 7, 9)
print(v1 * v2)  # Output should be 32



# Explanation:
Initialization (__init__):
The Vector class takes an arbitrary number of components as arguments and stores them in a tuple self.components.

Addition (__add__):
The __add__ method checks that the vectors are of the same dimension and then adds the corresponding components element-wise using a list comprehension. It returns a new Vector instance with the resulting components.

Dot Product (__mul__):
The __mul__ method calculates the dot product by multiplying corresponding components and summing the results. It returns a scalar value representing the dot product.

String Representation (__str__):
The __str__ method provides a human-readable representation of the vector.

This implementation handles vectors of arbitrary dimensions and ensures that operations are only performed on vectors of the same dimension, raising an error otherwise.



'''