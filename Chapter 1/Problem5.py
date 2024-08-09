import os

def list_directory_contents(path='.'):
    try:
        # Get the list of files and directories
        contents = os.listdir(path)
        # Print the contents
        for item in contents:
            print(item)
    except Exception as e:
        print(f"Error: {e}")

# Specify the directory path
directory_path = '.'  # Current directory
list_directory_contents(directory_path)
