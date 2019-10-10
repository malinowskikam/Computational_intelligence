import random
import numpy
import plotly.graph_objects as go


#a
def losuj(a, b):
    return random.randint(min(a, b), max(a, b))

x = [losuj(0,20) for i in range(100)]

data = {}

for i in range(21):
    data[i] = 0

for i in x:
    data[i] = data[i]+1

fig = go.Figure(
    data=go.Bar(x=tuple(data.keys()),y=tuple(data.values()))
)
fig.update_layout(
    title = "Losowanie liczb",
    xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="Liczby")),
    yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Liczba wystąpień")),
)
fig.show()