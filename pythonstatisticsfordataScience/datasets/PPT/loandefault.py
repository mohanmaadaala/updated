import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Load the dataset
file_path = r'C:\Users\mohan\Downloads\loan_default_data_200_customers.csv'
data = pd.read_csv(file_path)

# Check the first few rows and the column names
print("First 5 rows of the data:")
print(data.head())

print("\nColumn names in the dataset:")
print(data.columns)

# Check for missing values
print("\nMissing values:")
print(data.isnull().sum())

# Drop unnecessary columns if they exist
columns_to_drop = ['Customer_ID', 'Name']
data = data.drop(columns=[col for col in columns_to_drop if col in data.columns])

# Plotting the distribution of Loan_Status (Approved/Rejected)
sns.countplot(x='Loan_Default', data=data)
plt.title('Loan Default Distribution')
plt.show()

# Features and target
X = data[['Loan_Amount', 'Customer_Income', 'Credit_Score']]  # Features
y = data['Loan_Default']  # Target variable

# Split the dataset into training and testing sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predicting on the test data
y_pred = model.predict(X_test)

# Evaluate the model
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Visualize the confusion matrix
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt="d", cmap="Blues")
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
