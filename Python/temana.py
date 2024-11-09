import random
import math
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

def calculate_standard_deviation(numbers):
    mean = calculate_mean(numbers)
    squared_diff = [(x - mean) ** 2 for x in numbers]
    variance = sum(squared_diff) / len(numbers)
    return math.sqrt(variance)

def generate_temperature_data():
    start_date = datetime(2023, 6, 1)
    temperatures = []
    for i in range(30):
        date = start_date + timedelta(days=i)
        temp = random.uniform(15, 30)
        temperatures.append((date, round(temp, 1)))
    return temperatures

def analyze_temperatures(data):
    temps = [t[1] for t in data]
    mean_temp = calculate_mean(temps)
    std_dev = calculate_standard_deviation(temps)
    return mean_temp, std_dev

def plot_temperature_data(data, mean_temp, std_dev):
    dates = [t[0] for t in data]
    temps = [t[1] for t in data]

    plt.figure(figsize=(12, 6))
    plt.plot(dates, temps, marker='o', linestyle='-', linewidth=2, markersize=6)
    plt.axhline(y=mean_temp, color='r', linestyle='--', label='Mean')
    plt.axhline(y=mean_temp + std_dev, color='g', linestyle=':', label='Mean + Std Dev')
    plt.axhline(y=mean_temp - std_dev, color='g', linestyle=':', label='Mean - Std Dev')

    plt.fill_between(dates, mean_temp - std_dev, mean_temp + std_dev, alpha=0.2, color='g')

    plt.title('Daily Temperatures with Mean and Standard Deviation')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.legend()

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=5))
    plt.gcf().autofmt_xdate()  # Rotate and align the tick labels

    plt.tight_layout()
    plt.show()

# Main program
temperature_data = generate_temperature_data()
mean_temp, std_dev = analyze_temperatures(temperature_data)

print("Daily Temperature Data:")
for date, temp in temperature_data:
    print(f"{date.strftime('%Y-%m-%d')}: {temp}°C")

print(f"\nAverage Temperature: {mean_temp:.1f}°C")
print(f"Standard Deviation: {std_dev:.1f}°C")

print("\nInterpretation:")
print(f"On average, the daily temperature is {mean_temp:.1f}°C.")
print(f"The temperature typically varies by ±{std_dev:.1f}°C from the average.")
print(f"We can expect about 68% of days to have temperatures between {mean_temp - std_dev:.1f}°C and {mean_temp + std_dev:.1f}°C.")

# Plot the data
plot_temperature_data(temperature_data, mean_temp, std_dev)
