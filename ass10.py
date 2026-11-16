# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering

# Load dataset
data = pd.read_csv("sales_data_sample.csv", encoding="latin1")

# Select input columns
X = data[["SALES", "QUANTITYORDERED", "PRICEEACH"]]

# Preprocessing
X = X.dropna()

# Scale data
sc = StandardScaler()
X = sc.fit_transform(X)

# Elbow Method
wcss = []

for i in range(1, 11):
    km = KMeans(n_clusters=i, random_state=42, n_init=10)
    km.fit(X)
    wcss.append(km.inertia_)

# Plot Elbow Graph
plt.plot(range(1, 11), wcss, marker="o")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()

# K-Means Clustering
km = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans = km.fit_predict(X)

# Hierarchical Clustering
hc = AgglomerativeClustering(n_clusters=3)
hierarchical = hc.fit_predict(X)

# Display results
print("K-Means Clusters:", kmeans)
print("Hierarchical Clusters:", hierarchical)