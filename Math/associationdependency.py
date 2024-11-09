import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from scipy.stats import pearsonr, spearmanr
import seaborn as sns

# Create a DataFrame simulating data of income, savings, and age
data = {
    'Income': [40, 50, 60, 70, 80, 90, 55, 65, 75, 85],
    'Savings': [4, 5, 6, 8, 10, 12, 6, 7, 9, 11],
    'Age': [25, 35, 45, 50, 60, 65, 30, 40, 55, 62],
    'Loan Approved': [1, 1, 1, 1, 0, 0, 1, 0, 0, 0]  # 1 = Approved, 0 = Not Approved
}
df = pd.DataFrame(data)

# 1. Association and Dependence (Correlation as an example of association)

# Compute Pearson correlation between Income and Savings
correlation_income_savings, _ = pearsonr(df['Income'], df['Savings'])
print(f"Correlation between Income and Savings: {correlation_income_savings:.2f}")

# 2. Causation and Correlation

# Plot correlation between Income and Savings (visualizing correlation)
sns.scatterplot(x='Income', y='Savings', data=df)
plt.title('Income vs Savings (Correlation, Not Causation)')
plt.show()

# 3. Covariance (Direction of Linear Relationship)

# Compute Covariance between Income and Savings
covariance_income_savings = np.cov(df['Income'], df['Savings'])[0, 1]
print(f"Covariance between Income and Savings: {covariance_income_savings:.2f}")

# 4. Simpson's Paradox

# Group by Loan Approved and calculate means
grouped_means = df.groupby('Loan Approved').mean()

print("Mean Values by Loan Approval Status:")
print(grouped_means)

# Simpson's Paradox Example:
# Let's assume a scenario where loan approval rates seem different when looking at groups separately,
# but when combined, it gives a misleading trend.

# Approvals by Age and Savings (within different ranges)
df['Age Group'] = pd.cut(df['Age'], bins=[20, 40, 60, 80], labels=["Young", "Middle", "Old"])
df['Savings Group'] = pd.cut(df['Savings'], bins=[0, 5, 10, 15], labels=["Low", "Medium", "High"])

print("\nLoan Approval Rates by Age and Savings Groups:")
print(df.groupby(['Age Group', 'Savings Group'])['Loan Approved'].mean())

# 5. Clustering Techniques (K-Means Clustering)

# Normalize the data for clustering
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[['Income', 'Savings', 'Age']])

# K-Means Clustering with 2 clusters
kmeans = KMeans(n_clusters=2, random_state=0)
df['Cluster'] = kmeans.fit_predict(scaled_data)

# Plot the clusters
plt.scatter(df['Income'], df['Savings'], c=df['Cluster'], cmap='viridis')
plt.title('K-Means Clustering (Income vs Savings)')
plt.xlabel('Income')
plt.ylabel('Savings')
plt.show()

# Show the clusters
print("\nCluster Centers (Income, Savings, Age):")
print(kmeans.cluster_centers_)

