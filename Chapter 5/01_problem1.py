words = {
    "bimar" : "ill",
    "bura"  : "bad",
    "darwaja" : "gate",
    "padhai" :  "student",
    "achha"  : "good",

}
word = input("Enter the word we want the meaning of:  ")

print(words[word])

#using Chatgpt
#Suggestions for Improvement:
#Error Handling: If the user enters a word that is not in your dictionary (words), 
# your current code will raise a KeyError. To handle this gracefully,
#  you can use dict.get() method which allows you to provide a default value if the key is not found:

word = input("Enter the Hindi word you want the meaning of: ")
translation = words.get(word, "Word not found in dictionary")
print(translation)

#Case Insensitivity: Consider making the input case insensitive so that 
# "bimar", "Bimar", and "BIMAR" all return the same translation.
#You can achieve this by converting the user input to lowercase before searching in the dictionary:

word = input("Enter the Hindi word you want the meaning of: ").lower()
translation = words.get(word, "Word not found in dictionary")
print(translation)


#Looping: If you want to allow the user to look up multiple words without restarting the program, 
# you can wrap the input and translation logic in a loop:

while True:
    word = input("Enter the Hindi word you want the meaning of (or 'q' to quit): ").lower()
    if word == 'q':
        break
    translation = words.get(word, "Word not found in dictionary")
    print(translation)
