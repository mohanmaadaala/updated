import numpy as np
import matplotlib.pyplot as plt

# Step 1: Real-time example - Heights of adult men
mean_height = 175    # Mean height in cm
std_dev_height = 10  # Standard deviation in cm
sample_size = 1000   # Let's simulate 1000 people

# Generate random heights that follow a normal distribution
heights = np.random.normal(mean_height, std_dev_height, sample_size)

# Step 2: Plot the histogram of the height data
plt.figure(figsize=(10, 6))
count, bins, ignored = plt.hist(heights, bins=30, density=True, alpha=0.6, color='g', edgecolor='black')

# Step 3: Plot the normal distribution curve (theoretical)
xmin, xmax = plt.xlim()  # Get the current x-axis limits
x = np.linspace(xmin, xmax, 100)  # Generate 100 points between xmin and xmax
p = 1/(std_dev_height * np.sqrt(2 * np.pi)) * np.exp(-(x - mean_height)**2 / (2 * std_dev_height**2))  # PDF formula

# Plot the normal distribution curve
plt.plot(x, p, 'k', linewidth=2, label='Normal Distribution Curve')

# Step 4: Display mean and standard deviation
plt.axvline(mean_height, color='r', linestyle='dashed', linewidth=2, label=f'Mean = {mean_height} cm')
plt.axvline(mean_height - std_dev_height, color='b', linestyle='dashed', linewidth=2, label=f'Std Dev = {std_dev_height} cm')
plt.axvline(mean_height + std_dev_height, color='b', linestyle='dashed', linewidth=2)

# Step 5: Add labels and title
plt.title("Distribution of Heights (Mean and Standard Deviation)", fontsize=16)
plt.xlabel("Height (cm)", fontsize=14)
plt.ylabel("Density", fontsize=14)
plt.legend()

# Step 6: Show the plot
plt.show()
