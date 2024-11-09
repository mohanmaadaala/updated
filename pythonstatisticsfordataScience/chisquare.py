import numpy as np
import pandas as pd
import scipy.stats as stats

# Simulated data: Employment Type (rows) and Loan Approval (columns)
# Employment Types: Full-time, Part-time, Self-employed
# Loan Approval: Approved (Yes) and Not Approved (No)
# The 'Count' represents the number of people in each category

data = {
    'Employment Type': ['Full-time', 'Part-time', 'Self-employed', 'Full-time', 'Part-time', 'Self-employed'],
    'Loan Approved': ['Yes', 'Yes', 'No', 'No', 'No', 'Yes'],
    'Count': [60, 20, 15, 40, 30, 25]  # Counts of approvals and denials for each employment type
}

# Create a DataFrame
df = pd.DataFrame(data)

# 1. Create a contingency table to show the relationship between Employment Type and Loan Approval
contingency_table = pd.pivot_table(df, values='Count', index='Employment Type', columns='Loan Approved', aggfunc=np.sum)

print("Contingency Table:")
print(contingency_table)

# 2. Perform the Chi-Square Test of Independence
# The function returns: chi2 statistic, p-value, degrees of freedom, and the expected frequencies
chi2, p, dof, expected = stats.chi2_contingency(contingency_table)

# 3. Output the results of the test
print(f"\nChi-Square Statistic: {chi2:.2f}")
print(f"Degrees of Freedom: {dof}")
print(f"P-value: {p:.4f}")

# 4. Set the significance level
alpha = 0.05  # 5% significance level

# 5. Decision rule based on the P-value
if p < alpha:
    print("Reject the null hypothesis (H0): Loan approval is dependent on employment type.")
else:
    print("Fail to reject the null hypothesis (H0): Loan approval is independent of employment type.")

# 6. Show the expected frequencies under the assumption of independence
print("\nExpected Frequencies if Loan Approval and Employment Type were Independent:")
expected_df = pd.DataFrame(expected, index=contingency_table.index, columns=contingency_table.columns)
print(expected_df)
