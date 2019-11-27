from sklearn.cluster import KMeans
from common import *


print("KMEAN")
dataframe = get_dataframe()

clustering = KMeans(
    n_clusters=3,
    init='random',
    random_state=2109386512
)

clustering.fit(dataframe.drop('irisclass', axis=1))

clusters = {}

for row in dataframe.iterrows():
    row_values = [[row[1][0], row[1][1]]]
    cluster_index = str(clustering.predict(row_values)[0])

    if cluster_index not in clusters:
        clusters[cluster_index] = {'x': [], 'y': [], 'class': []}

    clusters[cluster_index]['x'].append(row[1][0])
    clusters[cluster_index]['y'].append(row[1][1])
    clusters[cluster_index]['class'].append(row[1][2])

#print_clusters_chart(clusters)
print(f"PURITY: {get_purity(clusters)}")
print(f"RAND: {get_rand_index(clusters)}")