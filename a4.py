# Clustering using K-Means

from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Data points
X = [
    [45, 50],
    [46, 48],
    [85, 90],
    [88, 92],
    [25, 30],
    [27, 28]
]

# Apply KMeans
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)

# Print cluster labels
print("Cluster Labels:")
print(kmeans.labels_)

# Plot clusters
plt.scatter(
    [x[0] for x in X],
    [x[1] for x in X],
    c=kmeans.labels_
)

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("K-Means Clustering")

plt.show()


# 1. What is clustering?
# Clustering is a technique used in machine learning to group similar data points together.
# It helps in identifying patterns or structures in data without predefined labels.
# Data points in the same cluster are more similar to each other than to others.
# 2. What type of learning is k-Means?
# k-Means is an unsupervised learning algorithm.
# It works on unlabeled data without any predefined output.
# The algorithm finds patterns and groups data automatically.
# 3. What does ‘k’ represent in k-Means?
# In k-Means, ‘k’ represents the number of clusters.
# It is a user-defined value given before running the algorithm.
# The data is divided into k distinct groups based on similarity.
# 4. How are centroids selected?
# Initially, centroids are selected randomly from the dataset.
# These centroids act as starting points for cluster formation.
# They are updated repeatedly during the algorithm process.
# 5. What is the objective of k-Means?
# The objective of k-Means is to minimize the distance between data points and centroids.
# It reduces the within-cluster variation (WCSS).
# This ensures that data points in the same cluster are closely related.
