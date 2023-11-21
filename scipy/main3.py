#Distribution of Sample Means
### GRADED
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import uniform, norm

dist1 = norm(loc=5 , scale=10)

sample_means = norm.rvs(loc=5, scale=10, size=500, random_state=22)
samples_30_or_more = []

for sample in sample_means:
    if sample >= 30:
        samples_30_or_more.append(sample)

samples_mean = np.mean(samples_30_or_more)
samples_std = np.std(samples_30_or_more)

plt.hist(samples_30_or_more, edgecolor = 'black', alpha = 0.3)
plt.title('Distribution of Sample Means');

# Answer check
print(type(samples_30_or_more))
print(samples_mean)
print(samples_std)