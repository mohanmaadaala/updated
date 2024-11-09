# Step 1: Ask the user for the number of scores
num_scores = int(input("How many scores do you want to enter? "))

# Step 2: Initialize total_score to 0 to store the sum of all scores
total_score = 0

# Step 3: Use a loop to ask for each score
for i in range(num_scores):
    score = float(input(f"Enter the score for student {i + 1}: "))
    total_score += score  # Add the score to total_score

# Step 4: Calculate the average score
average_score = total_score / num_scores

# Step 5: Check if the student passed or failed
if average_score >= 60:
    print(f"The average score is {average_score:.2f}. The student has Passed.")
else:
    print(f"The average score is {average_score:.2f}. The student has Failed.")
