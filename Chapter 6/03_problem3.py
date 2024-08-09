
s1 ="Make a lot of money" 
s2 ="buy now"
s3 ="subscribe this"
s4 ="click this"

message = input("Enter the comment: ").lower()

if((s1.lower() in message) or (s2.lower() in message) or (s3.lower() in message) or (s4.lower() in message)):
    print("The given message is Spam")

else:
    print("The message is not Spam")


 # Chatgpt suggestion
 
import re

# Define the list of spam keywords
spam_keywords = ["Make a lot of money", "buy now", "subscribe this", "click this"]

# Convert each keyword to lowercase for case-insensitive matching
spam_keywords_lower = [keyword.lower() for keyword in spam_keywords]

message = input("Enter the comment: ").lower()

# Create a regular expression pattern to match any of the spam keywords
pattern = r"\b(" + "|".join(re.escape(keyword) for keyword in spam_keywords_lower) + r")\b"

# Check if any spam keyword is found in the message
if re.search(pattern, message):
    print("The given message is Spam")
else:
    print("The message is not Spam")


