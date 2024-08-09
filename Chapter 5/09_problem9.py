s = {8, 7, 12, "Harry", [1,2]}

# No, you cannot directly change the values inside a list that is contained within a set in Python. 
# This is because sets in Python are designed to hold immutable elements, 
# and lists are mutable objects. 
# The presence of a mutable object like a list within a set could lead to unexpected behavior 
# if the set is mutated in a way that affects the internal state of the list.

# s = {8, 7, 12, "Harry", [1, 2]}
#TypeError: unhashable type: 'list'

#If you want to store collections of mutable objects where the order of elements is not important
#  and duplicates are not allowed, 
# consider using lists or tuples instead of sets. 
# Here's how you can use a tuple containing a list:

s = {8, 7, 12, "Harry", (1, 2)}


# Summary
#if mutability is crucial for your data structure,
#  consider using lists or other mutable collections directly instead of sets. 
# If you need to use sets for unique and immutable elements, 
# ensure that the elements themselves are immutable.
