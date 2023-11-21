

### GRADED
from scipy.stats import uniform
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

gauss1 = norm(loc=5, scale=2)

samples = norm.rvs(loc=5, scale=2, size=100, random_state=12)

#x = np.linspace(-5, 5, 1000)
# Create the distribution
mu = 5
sigma = 2

# Create the array
x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 1000)

plt.plot(x, gauss1.pdf(x), color = 'black', linewidth = 4, label = 'distribution')
plt.hist(samples, density=True, alpha = 0.2, bins = 10, edgecolor = 'black', label = 'sample')
plt.legend();


print(type(x))
print(len(x))
print(plt)

