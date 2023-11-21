#histogram of the salaries
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#read in the data
baseball_salaries = pd.read_csv('data/baseball.csv', index_col=0)

# Sample sizes to iterate through
sample_sizes = [5, 10, 25, 50, 100]
sample_means_list = []
sample_std_list = []

# Plotting histograms for different sample sizes on the same graph
plt.figure(figsize=(10, 6))  # Adjust figure size if needed
for sample_size in sample_sizes:
    sample_means = []


    for i in range(1000):
        sample = baseball_salaries['salary'].sample(sample_size)
        sample_mean = np.mean(sample)
        sample_means.append(sample_mean)
    
    plt.hist(sample_means, bins=30, alpha=0.5, label=f'Sample Size = {sample_size}')
    sample_means_list.append("${:,.2f}".format(np.mean(sample_means)))
    sample_std_list.append("${:,.2f}".format(np.std(sample_means)))

plt.xlabel('Sample Means')
plt.ylabel('Frequency')
plt.title('Histogram of Sample Means for Different Sample Sizes')
plt.axvline(np.mean(sample_means), color='red', linestyle='dashed', linewidth=1, label='Mean: '+ "${:,.2f}".format(np.mean(sample_means)) )
plt.legend()
plt.tight_layout()

# Saving the combined histogram as a single file
plt.savefig('combined_histogram.jpg')

# Show the combined plot
plt.show()

# Creating a DataFrame to store means and standard deviations
data = {
    'Sample Size': sample_sizes,
    'Mean': sample_means_list,
    'Standard Deviation': sample_std_list
}

df = pd.DataFrame(data)

# Plotting DataFrame as a table and saving it as an image
plt.figure(figsize=(8, 4))
plt.table(cellText=df.values,
          colLabels=df.columns,
          cellLoc='center',
          loc='upper left')
plt.axis('off')  # Hide the axis
plt.title('Means and Standard Deviations for Different Sample Sizes')
plt.tight_layout()

# Saving the table as an image file
plt.savefig('means_std_table_image.png')