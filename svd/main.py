import numpy as np
from scipy.linalg import svd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.datasets import fetch_openml

### GRADED
### Function to Standardize and Factor

def svd_norm(X):
    x_norm =( X - X.mean())/X.std()
    U, sigma, VT = svd(x_norm, full_matrices=False)
    Sigma = np.diag(sigma)
    return U, Sigma, VT
#
#
#
for i in range(5): #test for 10 random images
    X = faces_data.iloc[np.random.randint(0, 10)].values.reshape(64, 64)
    U, Sigma, VT = svd_norm(X)

# Answer check
U, Sigma, VT = svd_norm(image)
print(U.shape, Sigma.shape, VT.shape)


### GRADED
### Reconstructing the Image
Sigma_copy = None
simpler_image = None

U, Sigma, VT = svd_norm(image)
Sigma_copy = np.copy(Sigma)
Sigma_copy[5:, 5:] = 0
simpler_image = U@Sigma_copy@VT


# Answer check
print(simpler_image.shape)
plt.imshow(simpler_image)
plt.title('Image Reconstructed from first 5 Singular Values');


### Repeat for Tabular Data
U, Sigma, VT = svd_norm(df)



## Function to project into lower dimension `r`
def pca(X, r):
    x_norm =( X - X.mean())/X.std()
    U, sigma, VT = svd(x_norm, full_matrices=False)
    Sigma = np.diag(sigma)
    Ur = U[:, :r]
    Sigma_r = Sigma[:r, :r]
    return pd.DataFrame(Ur @ Sigma_r, columns = [f'pca_{i}' for i in range(1, r + 1)])

# Answer check
XT = pca(df, r = 2)
print(XT.shape)
XT.head()


### GRADED
newhome = pd.DataFrame([[3.87, 28.64, 5.43, 1.1, 1425.48, 3.07, 35.63, -119.57, 2.07]], columns = df.columns)
newhome


### BEGIN HIDDEN TESTS
normed_newhome = (newhome - df.mean())/df.std()

U, Sigma, VT = svd_norm(df)
ans5 = normed_newhome@VT.T[:, :2]

# Answer check
print(ans5.shape)
print(type(ans5))
ans5


### GRADED
### Extracting $\Sigma$

def singular_values(X, scale = False):
    """Return the singular values resulting from 
    SVD decomposition.  

    Parameters
    ----------
    X: np.array or pd.DataFrame
        An array of data
    scale: boolean
        Boolean determines whether data needs to be scaled

    Returns an numpy array of singular values of X
    """
    if isinstance(X, pd.DataFrame):
        X = X.values  # Convert DataFrame to numpy array
    
    if scale:
        # Scale the data if required
        mean = np.mean(X, axis=0)
        std = np.std(X, axis=0)
        X = (X - mean) / std
    
    U, Sigma, VT = np.linalg.svd(X, full_matrices=False)
    return Sigma

# Answer check
print(type(singular_values(df)))
sigma = singular_values(df)
print(sigma.shape)

def singular_values_(X, scale = False):
    if scale:
        X = (X - X.mean())/X.std()
        
    u, sigma, vt = svd(X)
    return sigma


#Scale the data set
### GRADED
# Assuming 'df' is your DataFrame with numeric columns to scale
numeric_columns = df.select_dtypes(include=np.number).columns.tolist()

# Calculate mean and standard deviation for each numeric column
mean_values = df[numeric_columns].mean()
std_values = df[numeric_columns].std()

# Scale the numeric columns manually
df_scaled = df.copy()  # Create a copy of the DataFrame

for col in numeric_columns:
    df_scaled[col] = (df[col] - mean_values[col]) / std_values[col]

# Answer check
print(type(df_scaled))

U, sigma, VT = svd(df_scaled)


# Assuming 'sigma' contains the singular values obtained from SVD
# Compute the sum of squares of singular values
sum_squares = np.sum(sigma ** 2)

# Compute the percent variance explained by each singular value
percent_variance_explained = (sigma ** 2) / sum_squares



print(percent_variance_explained.shape)
print(percent_variance_explained.sum())

### GRADED

# Assuming 'percent_variance_explained' contains the percentages of variance explained by each singular value

# Calculate the cumulative sum of explained variance
cumulative_variance = np.cumsum(percent_variance_explained)

# Find the number of principal components required to retain 80% of explained variance
num_components_for_80_percent_variance = np.argmax(cumulative_variance >= 0.8) + 1

# Assign the number of components as an integer to 'ans4'
ans4 = int(num_components_for_80_percent_variance)

print(type(ans4))
print(ans4)


### GRADED
ans1 = None

# Calculate the mean of the first column
mean_d1 = dist_df['d1'].mean()

# Find the index of the data point closest to the mean of the first column
ans1 = np.argmin(np.abs(dist_df['d1'] - mean_d1))

# Answer check
print(ans1)
print(type(ans1))

###3d plotting
plt.figure(figsize = (6,6))
ax = plt.axes(projection = '3d')
ax.scatter3D(default['AGE'], default['BILL_AMT1'], default['BILL_AMT2'], c = default['default.payment.next.month'], alpha = 0.4)
ax.set_xlabel('AGE', labelpad = 20)
ax.set_ylabel('Bill 1 Amount', labelpad = 20)
ax.set_zlabel('Bill 2 Amount', labelpad = 20)
ax.view_init(10, 60)
plt.title('Age and Bill Amount Colored by Default')
plt.tight_layout();

px.scatter_3d(data_frame=default, x = 'AGE', y = 'BILL_AMT1', z = 'BILL_AMT2', color = 'default.payment.next.month')

# Separate features and target variable
features = default.drop('default.payment.next.month', axis=1)
target = default['default.payment.next.month']

# Preprocessing: Standardize the features
scaler = StandardScaler()
features_standardized = scaler.fit_transform(features)

# Apply PCA for 2 dimensions
pca_2d = PCA(n_components=2)
data_pca_2d = pca_2d.fit_transform(features_standardized)

# Apply PCA for 3 dimensions
pca_3d = PCA(n_components=3)
data_pca_3d = pca_3d.fit_transform(features_standardized)

# Plotting
# Scatter plot for 2D PCA
plt.figure(figsize=(8, 6))
plt.scatter(data_pca_2d[:, 0], data_pca_2d[:, 1], c=target, cmap='viridis', alpha=0.5)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('2D PCA - Colored by Default Payment Next Month')
plt.colorbar()
plt.show()

# 3D PCA plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
sc = ax.scatter(data_pca_3d[:, 0], data_pca_3d[:, 1], data_pca_3d[:, 2], c=target, cmap='viridis', alpha=0.5)
ax.set_xlabel('Principal Component 1')
ax.set_ylabel('Principal Component 2')
ax.set_zlabel('Principal Component 3')
ax.set_title('3D PCA - Colored by Default Payment Next Month')
fig.colorbar(sc)
plt.show()

inertias = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X)
    inertias.append(kmeans.inertia_)