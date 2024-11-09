import pandas as pd
import matplotlib.pyplot as plt

# Load the apple quality dataset
df = pd.read_csv(r'C:\Users\mohan\Downloads\Healthcare-Diabetes.csv')




# Calculate the mean of 'SkinThickness', excluding zeros

mean_glucose = df['Glucose'][df['Glucose'] != 0].mean()
mean_bp= df['BloodPressure'][df['BloodPressure'] != 0].mean()

# Calculate the mean of 'Insulin', excluding zeros
mean_insulin = df['Insulin'][df['Insulin'] != 0].mode()

# Calculate the mean of 'BMI', excluding zeros
mean_bmi = df['BMI'][df['BMI'] != 0].mean()

# Replace zeros with the calculated mean in each column

df['Insulin'] = df['Insulin'].replace(0, mean_insulin)
df['BMI'] = df['BMI'].replace(0, mean_bmi)
df['BloodPressure'] = df['BloodPressure'].replace(0, mean_bp)
df['Glucose'] = df['Glucose'].replace(0, mean_glucose)


# Check the updated columns
print(df.describe())
plt.boxplot(df['Insulin'])

# Add a title and labels


# Display the plot
plt.show()

