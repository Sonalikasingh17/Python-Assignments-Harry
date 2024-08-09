# Repeat program 4 for a list of such words to be censored.

words = ["Donkey", "are", "Beauty"]

with open("file.txt", "r") as f:
    content =  f.read()

for word in words:
    content = content.replace(word, "#"* len(word))

with open("file.txt", "w") as f:
       f.write(content)


# Same thing as above only change is assigning each values to different values.
'''
words = ["Donkey", "are"]

with open("file.txt", "r") as f:
    content =  f.read()

for word in words:
    content = content.replace("Donkey","Horse")
    content = content.replace("is","are" )
with open("file.txt", "w") as f:
       f.write(content)
       '''