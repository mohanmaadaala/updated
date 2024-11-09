'''
import numpy as np
from scipy.stats import skew

# Consider numbers from 1 to 10
data = np.arange(1, 11)

# Calculate mean
mean_value = np.mean(data)

# Calculate median
median_value = np.median(data)

# Calculate skewness
skewness_value = skew(data)

# Calculate variance
variance_value = np.var(data)

# Calculate standard deviation
std_dev_value = np.std(data)

print("Mean:", mean_value)
print("Median:", median_value)
print("Skewness:", skewness_value)
print("Variance:", variance_value)
print("Standard Deviation:", std_dev_value)
'''
# Define the probabilities using events A and B
P_A = 2 / 52  # Probability of picking a black king
P_B_given_A = 1  # Probability that the card is black given it's a black king
P_B = 26 / 52  # Probability of picking a black card

# Apply Bayes' Theorem
P_A_given_B = (P_B_given_A * P_A) / P_B

P_A_given_B
