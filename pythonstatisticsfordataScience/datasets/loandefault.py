import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# Load the loan default dataset
df = pd.read_csv(r'C:\Users\mohan\Downloads\Loan_Default.csv')
pd.set_option('display.max_columns', None)

# Print the DataFrame summary
print(df.describe())
print(df.info())

# Boxplot for Loan Amount
plt.boxplot(x=df['LoanAmount'])
plt.title('Boxplot of Loan Amount')
plt.show()

# Create histograms comparing features with Default status, clustered by NumCreditLines
features_to_plot = ['Income', 'LoanAmount', 'CreditScore', 'InterestRate']

# Set up the matplotlib figure
plt.figure(figsize=(15, 10))

# Create a unique set of credit lines to iterate over
credit_lines = df['NumCreditLines'].unique()

# Create a color palette for Default status
palette = sns.color_palette("Set1", 2)  # Using a distinct palette for two categories

for feature in features_to_plot:
    plt.figure(figsize=(15, 5))
    
    # Create a histogram for the feature, colored by Default status
    sns.histplot(data=df, x=feature, hue='Default', multiple='stack', bins=30, kde=True, palette=palette)
    
    plt.title(f'Histogram of {feature} by Default Status')
    plt.xlabel(feature)
    plt.ylabel('Frequency')
    
    # Add a legend
    plt.legend(title='Default', loc='upper right', frameon=True)  # Ensure the legend is visible
    plt.tight_layout()  # Adjust layout to make room for the legend
    plt.show()

# Calculate the correlation matrix including only numeric variables
correlation_matrix = df.select_dtypes(include='number').corr()

# Create a heatmap for the correlation matrix
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".3f", cmap='coolwarm', square=True)
plt.title('Correlation Matrix Heatmap')
plt.show()

# Features and target variable for logistic regression
X = df[['Income', 'InterestRate', 'CreditScore', 'LoanAmount', 'NumCreditLines']]
y = df['Default']

# Split data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Initialize and train the model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)
