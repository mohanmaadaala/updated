import numpy as np
import pandas as pd
from scipy import stats
from sklearn.metrics import confusion_matrix
import math

# Sample dataset representing bank customers
data = {
    'Income': [45000, 54000, 58000, 61000, 49000, 68000, 72000, 30000, 75000, 80000],
    'Credit Score': [600, 700, 670, 720, 690, 650, 710, 520, 680, 730],
    'Loan Approved': [0, 1, 1, 1, 0, 1, 1, 0, 1, 1]  # 1 = Yes, 0 = No
}

# Load data into a DataFrame
df = pd.DataFrame(data)

# 1. Mean, Median, Mode

mean_income = df['Income'].mean()
median_income = df['Income'].median()
mode_income = df['Income'].mode()[0]

print(f"Mean Income: {mean_income}")
print(f"Median Income: {median_income}")
print(f"Mode Income: {mode_income}")

# 2. Sensitivity (Example: Loan Approval Sensitivity)
# Here, we assume sensitivity is measured using a simple binary classification (loan approved or not)

# Let's assume "1" is the positive class (Loan Approved), and "0" is the negative class (Loan Not Approved)
y_true = df['Loan Approved']  # Actual loan status
y_pred = [1, 1, 1, 1, 0, 1, 1, 0, 1, 1]  # Predicted loan status (for example purposes)

# Create confusion matrix
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# Sensitivity (True Positive Rate) = TP / (TP + FN)
sensitivity = tp / (tp + fn)
print(f"Sensitivity (Loan Approved): {sensitivity:.2f}")

# 3. Entropy (Calculate Entropy for Loan Approval)
def entropy(labels):
    """Calculate entropy of label distribution."""
    n_labels = len(labels)
    if n_labels <= 1:
        return 0
    value, counts = np.unique(labels, return_counts=True)
    probs = counts / n_labels
    n_classes = np.count_nonzero(probs)
    if n_classes <= 1:
        return 0
    return -np.sum(probs * np.log2(probs))

# Calculate entropy for the loan approval feature
loan_approval_entropy = entropy(df['Loan Approved'])
print(f"Loan Approval Entropy: {loan_approval_entropy:.4f}")

# 4. Information Gain (Using Income to Predict Loan Approval)
def information_gain(df, feature, target):
    """Calculate information gain of a feature."""
    total_entropy = entropy(df[target])
    values, counts = np.unique(df[feature], return_counts=True)
    weighted_entropy = np.sum(
        (counts[i] / np.sum(counts)) * entropy(df[df[feature] == values[i]][target]) for i in range(len(values))
    )
    return total_entropy - weighted_entropy

income_info_gain = information_gain(df, 'Income', 'Loan Approved')
print(f"Information Gain of Income for Loan Approval: {income_info_gain:.4f}")

