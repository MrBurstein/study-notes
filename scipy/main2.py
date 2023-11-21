####Comparing the sample means to actual
### GRADED
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import uniform, norm

dist1 = uniform(loc=5 , scale=10)

sample_means = uniform.rvs(loc=5, scale=10, size=500, random_state=22)


# Actual mean
true_mean = 10

# Sample size
sample_size = 400

# Calculate standard error of the mean
standard_deviation = np.std(sample_means)
standard_error = standard_deviation / np.sqrt(sample_size)

# Check if the error is less than 0.1
error_threshold = 0.1
ans3 = standard_error < error_threshold


plt.plot(range(1, 501), sample_means, label = 'sample mean', color = 'purple')
plt.axhline(10, label = 'true mean', color = 'green')
plt.xlabel('Sample Size')
plt.legend();


# Answer check
print(type(ans3))
print(ans3)