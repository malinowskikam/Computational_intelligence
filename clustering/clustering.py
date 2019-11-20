import numpy
from sklearn.cluster import KMeans
import pandas
import plotly.graph_objects as go

dataframe = pandas.read_csv("iris2D.csv").drop('id', axis=1).apply(pandas.to_numeric)

clustering = KMeans(
    n_clusters=3,
    init='random',
    random_state=2109386512
)

clustering.fit(dataframe)

clusters = {
    '0': {
        'x': [],
        'y': []
    },
    '1': {
        'x': [],
        'y': []
    },
    '2': {
        'x': [],
        'y': []
    },
}

for row in dataframe.iterrows():
    row_values = [[row[1][0], row[1][1]]]
    cluster_index = str(clustering.predict(row_values)[0])
    print(cluster_index)
    clusters[cluster_index]['x'].append(row_values[0][1])
    clusters[cluster_index]['y'].append(row_values[0][0])

fig = go.Figure()
# Add traces
fig.add_trace(go.Scatter(x=clusters['0']['x'], y=clusters['0']['y'],mode='markers',name='Klaster "0"'))
fig.add_trace(go.Scatter(x=clusters['1']['x'], y=clusters['1']['y'],mode='markers',name='Klaster "1"'))
fig.add_trace(go.Scatter(x=clusters['2']['x'], y=clusters['2']['y'],mode='markers',name='Klaster "2"'))

fig.show()