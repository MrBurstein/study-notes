import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler
import warnings

#Prepare Data
object_cols = df.select_dtypes('object').columns.tolist()
#Drop 'Object' Data
df_numeric = df.drop(object_cols, axis = 1)
#Drop non informative
object_cols = df.select_dtypes('object').columns.tolist() 
df_clean = df.drop(object_cols, axis = 1)
#Drop the missing data
object_cols = df.select_dtypes('object').columns.tolist() 
df_clean = df.drop(object_cols, axis = 1)
df_clean_nona = df_clean.dropna()
#Scale the data
df_scaled = (df_clean_nona - df_clean_nona.mean())/df_clean_nona.std()
#PCA
pca = PCA(n_components=3, random_state=42)
#Extract the components
pca = PCA(n_components=3, random_state = 42)
components = pca.fit_transform(df_scaled)

# DBSCAN
dbscan = DBSCAN(eps=0.5, min_samples=5)  # Adjust parameters as needed
dbscan.fit(components)

# Plotting clusters in 3D space
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

scatter = ax.scatter(components[:, 0], components[:, 1], components[:, 2], c=dbscan.labels_, cmap='viridis')
ax.set_title('Clusters based on PCA Components (DBSCAN)')
ax.set_xlabel('Component 1')
ax.set_ylabel('Component 2')
ax.set_zlabel('Component 3')
ax.legend(*scatter.legend_elements(), title='Clusters')
plt.show()