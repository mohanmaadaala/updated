import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv(r'C:\Users\mohan\Downloads\filtered_data_month_1.csv')
print(df.describe())

print(df.head())

plt.scatter(x=df['total_amount'],y=df['trip_distance'])
plt.show()

# Create pair plots for the DataFrame
sns.pairplot(df)
plt.show()

plt.boxplot(x=df['fare_amount'])
plt.show()



# Create a label encoder object



# Calculate the correlation matrix, selecting only numeric columns
correlation_matrix = df.select_dtypes(include=[np.number]).corr()

# Create a heatmap with 'Purchased' as the dependent variable
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix[['total_amount']], annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation with total_amount')
plt.show()

# Step 3: Data Preparation
# Selecting the dependent variables and independent variable
X = data[['fare_amount', 'trip_distance', 'tolls_amount', 'trip_duration', 'hour_of_day']]
y = data['total_amount']

# Step 4: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Model Creation
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Get Coefficients and Intercept
coefficients = model.coef_
intercept = model.intercept_

# Print Coefficients and Intercept
print("Intercept:", intercept)
print("Coefficients:")
for feature, coef in zip(X.columns, coefficients):
    print(f"{feature}: {coef}")

# Step 7: Model Evaluation
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\nRoot Mean Squared Error (RMSE):", rmse)
print("R² Score:", r2)

# Step 8: Visualization

# Visualization 1: Actual vs Predicted Total Amount
plt.figure(figsize=(10, 6))
sns.scatterplot(x=y_test, y=y_pred, alpha=0.6)
plt.xlabel("Actual Total Amount")
plt.ylabel("Predicted Total Amount")
plt.title("Actual vs Predicted Total Amount")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'k--', lw=2)  # Diagonal line
plt.show()

# Visualization 2: Relationship between Total Amount and Each Feature
for feature in X.columns:
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=data[feature], y=data['total_amount'], alpha=0.6)
    plt.xlabel(feature)
    plt.ylabel("Total Amount")
    plt.title(f"Total Amount vs {feature}")
    plt.show()