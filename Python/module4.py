import random  # For generating a random student ID
import datetime  # For capturing the current registration time
import json  # For converting student data to JSON format
import re  # For validating student name (no digits allowed)
import os  # For checking file path

# Step 1: Generate a random student ID
student_id = random.randint(1000, 9999)  # Generate a random student ID between 1000 and 9999
print(f"Generated Student ID: {student_id}")

# Step 2: Record the current registration time
registration_time = datetime.datetime.now()  # Get the current date and time
print(f"Registration Time: {registration_time}")

# Step 3: Get student name and age
student_name = input("Enter student name (no digits allowed): ")
student_age = input("Enter student age: ")

# Step 4: Validate student name using regular expressions (name shouldn't contain numbers)
if re.search(r'\d', student_name):
    print("Error: Name should not contain numbers.")
else:
    print(f"Student Name: {student_name}")

# Step 5: Store student data in JSON format
student_data = {
    "student_id": student_id,
    "name": student_name,
    "age": student_age,
    "registration_time": str(registration_time)  # Convert datetime to string for JSON
}
student_json = json.dumps(student_data)  # Convert dictionary to JSON format
print(f"Student Data (JSON): {student_json}")

# Step 6: Save the student data to a file (handle exceptions)
try:
    # File name where the student data will be saved
    file_path = 'student_registration.json'

    # Open the file in write mode (create it if it doesn't exist)
    with open(file_path, 'w') as file:
        file.write(student_json)  # Write the JSON data to the file

    print(f"Student data saved successfully to {file_path}")
except FileNotFoundError:
    print("Error: The file could not be found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
