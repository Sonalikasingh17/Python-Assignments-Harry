# Override the __len__() method on vector of problem 5 to display the dimension of the vector

class Vector:
    def __init__(self, list):
        self.list = list
    
    def __len__(self):
        return len(self.list)
    
#Test the implementation
v1 = Vector([2, 3, 4])
print(len(v1))