import os
import math

# Input text with multiple paragraphs (can be dynamic or read from a source)
input_text = """This is the first paragraph.
It contains several sentences that form the first unit of content.

This is the second paragraph.
It has its own structure and makes a different point.

This is the third paragraph, which may be smaller or larger than others.

This is the fourth paragraph with more information."""

# Step 1: Split the input text by paragraphs (assuming paragraphs are separated by two newlines)
paragraphs = input_text.split("\n\n")

# Step 2: Decide the number of files (you can specify this number)
num_files = 2  # For example, we'll split content into 2 files

# Step 3: Calculate how many paragraphs per file
paragraphs_per_file = math.ceil(len(paragraphs) / num_files)

# Step 4: Create files and distribute the content equally
output_folder = r"C:\Users\mohan\Documents"  # Change this to your desired folder

for i in range(num_files):
    # Create a file for each chunk
    file_path = os.path.join(output_folder, f"output_file_{i + 1}.txt")
    
    with open(file_path, "w") as file:
        # Calculate start and end index for paragraphs in this file
        start_idx = i * paragraphs_per_file
        end_idx = start_idx + paragraphs_per_file
        
        # Write the chunk of paragraphs to the file
        file.write("\n\n".join(paragraphs[start_idx:end_idx]))
    
    print(f"File 'output_file_{i + 1}.txt' created with content from paragraph {start_idx + 1} to {min(end_idx, len(paragraphs))}.")

