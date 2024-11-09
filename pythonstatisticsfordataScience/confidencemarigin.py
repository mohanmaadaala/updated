import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Sample Data: Loan approval rates (1 = Approved, 0 = Not Approved)
loan_approval = np.array([1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1])

# 1. Point Estimation (Sample Mean)
sample_size = len(loan_approval)
sample_mean = np.mean(loan_approval)

print(f"Point Estimation (Sample Mean of Loan Approval): {sample_mean:.2f}")

# 2. Confidence Interval (Using 95% Confidence Level)
confidence_level = 0.95
alpha = 1 - confidence_level

# Standard Error of the sample mean
std_err = np.std(loan_approval, ddof=1) / np.sqrt(sample_size)

# Confidence Interval using t-distribution (appropriate for small samples)
t_critical = stats.t.ppf(1 - alpha/2, df=sample_size - 1)
margin_of_error = t_critical * std_err

lower_bound = sample_mean - margin_of_error
upper_bound = sample_mean + margin_of_error

print(f"95% Confidence Interval: [{lower_bound:.2f}, {upper_bound:.2f}]")

# 3. Hypothesis Testing
# Null Hypothesis (H0): Loan approval rate = 50% (or 0.50)
# Alternative Hypothesis (H1): Loan approval rate ≠ 50%

# Assumed population proportion under null hypothesis (p0)
p0 = 0.50

# Calculate z-statistic for hypothesis testing
z_statistic = (sample_mean - p0) / std_err

# p-value for two-tailed test
p_value = 2 * (
