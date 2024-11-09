import numpy as np
import pandas as pd
from collections import Counter
from scipy.stats import entropy
from math import log2

# Step 1: Generate a dataset
data = {
    'Customer': ['C1', 'C2', 'C3', 'C4', 'C5'],
    'Income': [60000, 35000, 40000, 45000, 50000], # Income in dollars
    'CreditScore': [750, 600, 650, 500, 700], # Credit Score
    'LoanAmount': [20000, 10000, 15000, 10000, 30000], # Loan Amount in dollars
    'Defaulted': [0, 1, 0, 1, 0]  # 0: Not Defaulted, 1: Defaulted
}

# Create a DataFrame
df = pd.DataFrame(data)

# Step 2: Calculate Mean, Median, and Mode
mean_income = df['Income'].mean()
median_income = df['Income'].median()
mode_income = Counter(df['Income']).most_common(1)[0][0]  # Mode calculation

mean_credit = df['CreditScore'].mean()
median_credit = df['CreditScore'].median()
mode_credit = Counter(df['CreditScore']).most_common(1)[0][0]

print(f"Mean Income: {mean_income}, Median Income: {median_income}, Mode Income: {mode_income}")
print(f"Mean Credit Score: {mean_credit}, Median Credit Score: {median_credit}, Mode Credit Score: {mode_credit}")

# Step 3: Apply Bayes' Theorem to Predict Default Based on Credit Score

# P(A): Probability of default (prior)
P_A = df['Defaulted'].mean()  # Total probability of default (prior)

# P(B|A): Probability of low credit score (<650) given default
low_credit_given_default = df[(df['Defaulted'] == 1) & (df['CreditScore'] < 650)].shape[0] / df[df['Defaulted'] == 1].shape[0]

# P(B): Probability of low credit score overall
low_credit_overall = df[df['CreditScore'] < 650].shape[0] / df.shape[0]

# Using Bayes' Theorem: P(A|B) = (P(B|A) * P(A)) / P(B)
P_A_given_B = (low_credit_given_default * P_A) / low_credit_overall

print(f"Probability of Default Given Low Credit Score (Bayes' Theorem): {P_A_given_B:.2f}")

# Step 4: Sensitivity (True Positive Rate)
true_positives = df[(df['Defaulted'] == 1) & (df['CreditScore'] < 650)].shape[0]
false_negatives = df[(df['Defaulted'] == 1) & (df['CreditScore'] >= 650)].shape[0]
sensitivity = true_positives / (true_positives + false_negatives)
print(f"Sensitivity (True Positive Rate): {sensitivity:.2f}")

# Step 5: Entropy and Information Gain

# Entropy function to handle cases where probability is 0
def calculate_entropy(p):
    return -p * log2(p) if p > 0 else 0

# Calculate entropy for default (0 and 1)
p_default = df['Defaulted'].mean()
p_non_default = 1 - p_default
entropy_default = calculate_entropy(p_default) + calculate_entropy(p_non_default)

print(f"Entropy of Default: {entropy_default:.3f}")

# Information Gain: After splitting based on CreditScore
# Split into two groups: CreditScore < 650 and CreditScore >= 650
low_credit_df = df[df['CreditScore'] < 650]
high_credit_df = df[df['CreditScore'] >= 650]

# Entropy of each group
p_default_low_credit = low_credit_df['Defaulted'].mean()
p_non_default_low_credit = 1 - p_default_low_credit
entropy_low_credit = calculate_entropy(p_default_low_credit) + calculate_entropy(p_non_default_low_credit)

p_default_high_credit = high_credit_df['Defaulted'].mean()
p_non_default_high_credit = 1 - p_default_high_credit
entropy_high_credit = calculate_entropy(p_default_high_credit) + calculate_entropy(p_non_default_high_credit)

# Weighted entropy after the split
weighted_entropy = (len(low_credit_df) / len(df)) * entropy_low_credit + (len(high_credit_df) / len(df)) * entropy_high_credit

# Information Gain
info_gain = entropy_default - weighted_entropy

print(f"Information Gain after splitting on Credit Score: {info_gain:.3f}")

# Outputting the DataFrame for Reference
print("\nCustomer Data:")
print(df)
