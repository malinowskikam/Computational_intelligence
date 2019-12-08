import pandas
import plotly.graph_objects as go
from sklearn.metrics import adjusted_rand_score


def get_dataframe():
    dataframe = pandas.read_csv("iris2D.csv").drop('id', axis=1).apply(pandas.to_numeric)
    dataframe_classes = pandas.read_csv("iris.csv")
    dataframe = dataframe.merge(dataframe_classes['irisclass'], left_index=True, right_index=True)

    return dataframe

def print_clusters_chart(clusters):
    fig = go.Figure()

    for index in clusters:
        fig.add_trace(go.Scatter(
            x=clusters[index]['x'],
            y=clusters[index]['y'],
            mode='markers',
            name=f'Cluster "{index}"'
        ))

    fig.show()

def get_cluster_class_map(clusters):
    map = dict()

    for cluster in clusters:

        counts = {
            'Iris-setosa': 0,
            'Iris-versicolor': 0,
            'Iris-virginica': 0
        }

        for actual_class in clusters[cluster]['class']:
            counts[actual_class] += 1

        map[cluster] = { 'class' : max(counts, key=counts.get), 'len' : sum(counts.values()) }
        map[cluster]['count'] = counts[map[cluster]['class']]

    return map


def get_purity(clusters):
    cluster_map = get_cluster_class_map(clusters)

    lens = []
    positives = []

    for cluster in cluster_map:
        if cluster != '-1':
            lens.append(cluster_map[cluster]['len'])
            positives.append(cluster_map[cluster]['count'])

    n_of_data_points = sum(lens)
    sum_of_positives = sum(positives)

    return sum_of_positives / n_of_data_points

def get_rand_index(clusters,labeling):
    cluster_map = get_cluster_class_map(clusters)
    dataframe = get_dataframe()['irisclass']

    for cluster in cluster_map:
        if(cluster_map[cluster]['class'] != '-1'):
            dataframe = dataframe.replace(cluster_map[cluster]['class'],cluster)

    dataframe = dataframe.replace("Iris",-2,regex=True).apply(pandas.to_numeric)


    return adjusted_rand_score(dataframe,labeling)