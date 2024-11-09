'''Male is encoded as 1
Female is encoded as 0
Books is encoded as 0
Electronics is encoded as 1
Clothing is encoded as 2
Tablet is encoded as 0
Desktop is encoded as 1
Mobile is encoded as 2
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv(r'C:\Users\mohan\Downloads\transformed_ecommerce_dataset.csv')
print(df.describe())
label_encoder = LabelEncoder()

# Encode 'Gender'
df['Gender'] = label_encoder.fit_transform(df['Gender'])

# Encode 'Product_Category'
df['Product_Category'] = label_encoder.fit_transform(df['Product_Category'])

# Encode 'Device_Used'
df['Device_Used'] = label_encoder.fit_transform(df['Device_Used'])

plt.boxplot(x=df['Age'])
plt.show()

# Display DataFrame after label encoding
print("\nDataFrame after Label Encoding:")
print(df)
print(df.head())

'''plt.scatter(x=df['Purchased'],y=df['Gender'])
plt.show()'''

'''# Create pair plots for the DataFrame
sns.pairplot(df)
plt.show()'''

'''plt.boxplot(x=df['Age'])
plt.show()'''



# Create a label encoder object



# Calculate the correlation matrix, selecting only numeric columns
correlation_matrix = df.select_dtypes(include=[np.number]).corr()

# Create a heatmap with 'Purchased' as the dependent variable
plt.figure(figsize=(10, 8))

sns.heatmap(correlation_matrix[['Purchased']], annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation with Purchased')
plt.show()

# Define independent variables (X) and the target variable (y)
X = df[['Age','Gender','Time_Spent','Product_Category','Number_of_Items_Viewed','Device_Used']]
y = df['Purchased']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the logistic regression model
model = LogisticRegression(max_iter=200)  # Increase max_iter if needed
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Set up the plotting style
sns.set(style="whitegrid")

# 1. Product Category by Gender
transformed_data_path = 'C:\\Users\\mohan\\Downloads\\transformed_ecommerce_dataset.csv'  # Update with the correct path
transformed_data = pd.read_csv(transformed_data_path)
plt.figure(figsize=(10, 6))
sns.countplot(data=transformed_data, x='Product_Category', hue='Gender', palette='viridis')
plt.title("Product Category Preferences by Gender")
plt.xlabel("Product Category")
plt.ylabel("Count")
plt.legend(title='Gender')
plt.show()

# 2. Purchase Likelihood by Time Spent
# Create bins for time spent to categorize users into groups
transformed_data['Time_Spent_Binned'] = pd.cut(transformed_data['Time_Spent'], bins=[0, 10, 20, 30, 40, 50, 60], labels=['0-10', '10-20', '20-30', '30-40', '40-50', '50-60'])
purchase_rate = transformed_data.groupby('Time_Spent_Binned')['Purchased'].mean() * 100

# Bar plot for average purchase rate per time spent bin
plt.figure(figsize=(10, 6))
sns.barplot(x=purchase_rate.index, y=purchase_rate.values, palette='coolwarm')
plt.title("Purchase Rate by Time Spent on Website")
plt.xlabel("Time Spent (minutes)")
plt.ylabel("Purchase Rate (%)")
plt.show()