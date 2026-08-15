import sklearn as sk, matplotlib.pyplot as plt, seaborn as sns

X, y = sk.datasets.make_blobs(n_samples=1000, n_features=5, random_state=0, shuffle=True)
WCSS = []

for k in range(1, 11):
    KMeans = sk.cluster.KMeans(n_clusters=k, random_state=0)
    KMeans.fit(X)
    WCSS.append(KMeans.inertia_)

sns.lineplot(x=range(1, 11), y=WCSS, markers='8')
plt.xlabel("Number of clusters")
plt.ylabel("WCSS")
plt.title("Elbow plot")
plt.show()

kmeans = sk.cluster.KMeans(n_clusters=len(set(y)), random_state=0)
labels = kmeans.fit_predict(X)

sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=y, palette="muted")
sns.scatterplot(x=kmeans.cluster_centers_[:, 0], y=kmeans.cluster_centers_[:, 1], color="black")
plt.show()

print(f"ELBOW ALGORITHM\nClusters: {len(set(y))}\nk-Means Within-Cluster Sum of Squares: {sum(WCSS)}")