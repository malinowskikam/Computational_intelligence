from sklearn.cluster import DBSCAN
from common import *


print("DBSCAN")
dataframe = get_dataframe()

clustering = DBSCAN(
    eps=1, # The maximum distance between two samples for one to be considered as in the neighborhood of the other
    min_samples=5 # The number of samples in a neighborhood for a point to be considered as a core point.
)

clustering.fit(dataframe.drop('irisclass', axis=1))

clusters = {}

for index in range(len(clustering.labels_)):
    cluster_index = str(clustering.labels_[index])

    if cluster_index not in clusters:
        clusters[cluster_index] = {'x': [], 'y': [], 'class': []}

    clusters[cluster_index]['x'].append(dataframe.iloc[index]['PC1'])
    clusters[cluster_index]['y'].append(dataframe.iloc[index]['PC2'])
    clusters[cluster_index]['class'].append(dataframe.iloc[index]['irisclass'])



print_clusters_chart(clusters)
print(f"PURITY: {get_purity(clusters)}")
print(f"RAND: {get_rand_index(clusters,clustering.labels_)}")
