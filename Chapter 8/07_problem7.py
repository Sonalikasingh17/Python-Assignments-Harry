# Write a python function to remove a given word from a list and strip it at the same time.

def remove(l, word):
    n = []
    for item in l:
       if not(item == word):
           n.append(item.strip(word))
    return n
    
l = ["Sohan", "Rohan", "Nisha","disha","dhruv", "Mona","Sona","Madhu", "Kashish","Sapna","Amrit","Nashra", "sh"]

print(remove(l,"sh"))

# Write a python function to remove a given word from a list 

# def remove(l, word):
#     for item in l:
#         l.remove(word)
#         return l
    
# l = ["Sohan", "Rohan", "Nisha","disha","dhruv", "Mona","Sona","Madhu", "Kashish","Sapna","Amrit","Nashra", "sh"]

# print(remove(l,"sh")) 
