# read a python program to rename a file to “renamed_by_ python.txt.

with open("old.txt", "r") as f:
    content = f.read()

with open("renamed_by_python.txt" , "w") as f:
     f.write(content)
   
# Chatgpt Suggestion
# By using OS module
import os

# Specify the original file name
original_file_name = "example.txt"

# Specify the new file name
new_file_name = "renamed_by_python.txt"

try:
    # Rename the file
    os.rename(original_file_name, new_file_name)
    print(f"The file has been renamed to {new_file_name}")
except FileNotFoundError:
    print(f"The file '{original_file_name}' does not exist.")
except PermissionError:
    print("You don't have permission to rename this file.")
except Exception as e:
    print(f"An error occurred: {e}")

'''
Explanation:
Importing the os Module: The os module is necessary for interacting with the operating system, such as renaming files.
Original and New File Names: Specify the original_file_name (the file you want to rename) and the new_file_name (the new name you want to give to the file).
Renaming the File: The os.rename() function takes two arguments: the current file name and the new file name. It renames the file from the first argument to the second.

Error Handling: The try-except block handles potential errors:
FileNotFoundError: If the original file does not exist.
PermissionError: If the program does not have permission to rename the file.
Exception: Any other unexpected errors.

Make sure to replace example.txt with the actual name of the file you want to rename. Additionally, ensure that the script has the necessary permissions and the file exists in the working directory or provide the full path to the file.
'''

# By using shutil module
import shutil

# Specify the original file name
original_file_name = "example.txt"

# Specify the new file name
new_file_name = "renamed_by_python.txt"

try:
    # Rename the file
    shutil.move(original_file_name, new_file_name)
    print(f"The file has been renamed to {new_file_name}")
except FileNotFoundError:
    print(f"The file '{original_file_name}' does not exist.")
except PermissionError:
    print("You don't have permission to rename this file.")
except Exception as e:
    print(f"An error occurred: {e}")

'''
Explanation:
Importing the shutil Module: The shutil module is imported to use the move() function.
Original and New File Names: original_file_name is the current name of the file you want to rename, and new_file_name is the desired new name.
Renaming the File: shutil.move() is used to rename the file. It takes two arguments: the current file path and the new file path (or new name).

Error Handling: The try-except block handles potential errors, such as:
FileNotFoundError: If the specified file does not exist.
PermissionError: If the program does not have the necessary permissions.
Exception: Catches any other exceptions that may occur during the operation.

Make sure to replace example.txt with the actual name of the file you want to rename and ensure that the file exists in the specified location.
'''