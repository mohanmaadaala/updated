import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Load the dataset
file_path = "C:\\Users\\mohan\\Downloads\\loan_default_data_200_customers_with_names.csv"
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("Data Preview:")
print(data.head())

# Check for missing values
print("\nMissing values:")
print(data.isnull().sum())

# Drop unnecessary columns
data.drop(columns=['Customer_ID', 'Name'], inplace=True)

# Encode categorical variables
data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})
data['Loan_Status'] = data['Loan_Status'].map({'Approved': 1, 'Rejected': 0})

# Define features (X) and target (y)
X = data.drop(columns=['Loan_Status'])
y = data['Loan_Status']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a Logistic Regression model
model = LogisticRegression()

# Fit the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Visualize the results
plt.figure(figsize=(8, 6))
sns.countplot(data=data, x='Loan_Status', palette='Set2')
plt.title('Loan Approval Status Distribution')
plt.xlabel('Loan Status')
plt.ylabel('Count')
plt.xticks([0, 1], ['Rejected', 'Approved'])
plt.show()
