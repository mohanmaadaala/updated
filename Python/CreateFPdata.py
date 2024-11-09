import os

# Hardcoded folder path and file name
folder_name = r"C:\Users\YourUsername\Documents"  # Change to your actual folder path
file_name = "example.txt"  # Change to your actual file name

# Build the full file path
file_path = os.path.join(folder_name, file_name)

# Check if the file exists
if os.path.exists(file_path):
    # If file exists, read its content
    with open(file_path, "r") as file:
        content = file.read()
        print("File found and its contents are:")
        print(content)
else:
    # If file is not found, create a new file and write data to it
    print(f"File '{file_name}' not found in folder '{folder_name}', creating a new file...")
    
    # Create the file and write some initial data
    with open(file_path, "w") as file:
        file.write("This is a new file created because the original was not found.\n")
        file.write("You can add more data here.\n")
    
    print(f"New file '{file_name}' created and data has been written to it.")

