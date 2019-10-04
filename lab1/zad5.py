import plotly
import csv

lata = []
gdansk = []
poznan = []
szczecin = []

with open("ludnosc.csv") as file:
    reader = csv.reader(file, 'excel', delimiter=',')
    next(reader)
    for line in reader:
        lata.append(int(line[0]))
        gdansk.append(int(line[1]))
        poznan.append(int(line[2]))
        szczecin.append(int(line[3]))

figure = plotly.graph_objs.Figure()
figure.add_trace(plotly.graph_objs.Scatter(x=lata, y=gdansk, mode='lines+markers', name="Gdansk"))
figure.add_trace(plotly.graph_objs.Scatter(x=lata, y=poznan, mode='lines+markers', name="Poznan"))
figure.add_trace(plotly.graph_objs.Scatter(x=lata, y=szczecin, mode='lines+markers', name="szczecin"))
figure.update_layout(showlegend=True)
figure.show()
