import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load data (ensure file path or dataframe is set correctly)
df = pd.read_csv(r'C:\Users\mohan\Downloads\Metro_Interstate_Traffic_Volume.csv')

# Convert 'holiday' column to 0 (for "None") and 1 (for other holidays)
df['holiday'] = np.where(df['holiday'] == 'None', 0, 1)

# Convert 'weather_main' column to numeric categories
df['weather_main'] = pd.Categorical(df['weather_main']).codes

df['date_time'] = pd.to_datetime(df['date_time'], dayfirst=True)

# Extract the hour for 'time' feature
df['time'] = df['date_time'].dt.hour

# Verify conversion by checking the first few rows
print(df[['date_time', 'time']].head())

# Select relevant columns
features = ['holiday', 'temp', 'rain_1h', 'snow_1h', 'clouds_all', 'weather_main', 'time']
X = df[features]
y = df['traffic_volume']

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Initialize and fit the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Print intercept and coefficients
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)

# Visualization of predicted vs. actual values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)
plt.xlabel('Actual Traffic Volume')
plt.ylabel('Predicted Traffic Volume')
plt.title('Actual vs. Predicted Traffic Volume')
plt.show()

# Residual plot
plt.figure(figsize=(10, 6))
sns.histplot(y_test - y_pred, kde=True, bins=30, color='skyblue')
plt.xlabel('Residuals')
plt.ylabel('Frequency')
plt.title('Residual Distribution')
plt.show()

# Calculate and print model evaluation metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("R^2 Score:", r2)
