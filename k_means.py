import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12, 15, 7, 11, 14, 8, 9, 15, 14, 4, 6, 5, 11, 12, 7, 9]
y = [21, 19, 18, 24, 24, 17, 16, 25, 24, 22, 21, 21, 17, 18, 19, 20, 17, 19, 21, 20 , 20, 22, 21, 23, 17]

plt.scatter(x, y)
plt.show()
print("\n")
data = list(zip(x, y))
inertias = []

for i in range(1,26):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

plt.plot(range(1,26), inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()
print("\n")
kmeans = KMeans(n_clusters=3)
kmeans.fit(data)

plt.scatter(x, y, c=kmeans.labels_)
plt.show()