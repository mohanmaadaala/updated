import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the apple quality dataset
df = pd.read_csv(r'C:\Users\mohan\Downloads\Student_performance_data _.csv')
pd.set_option('display.max_columns', None)

# Now print the DataFrame or summary to see all columns
print(df.describe())
sns.pairplot(df)
plt.show()
# Create subplots for each column
columns = ['StudyTimeWeekly', 'Absences', 'ParentalSupport']

# Generate separate boxplots for each column
for i, col in enumerate(columns, 1):
    plt.subplot(2, 2, i)  # 2 rows, 2 columns
    sns.boxplot(data=df, y=col, color='lightblue')
    plt.title(f'Boxplot for {col}')
    plt.ylabel(col)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()