import random
import numpy

from deap import base
from deap import creator
from deap import tools
from deap import algorithms

import plotly.graph_objects as go

items = [
    {'name': 'zegar', 'value': 100, 'weight': 7},
    {'name': 'obraz-pejzaż', 'value': 300, 'weight': 7},
    {'name': 'obraz-portret', 'value': 200, 'weight': 6},
    {'name': 'radio', 'value': 40, 'weight': 2},
    {'name': 'laptop', 'value': 500, 'weight': 5},
    {'name': 'lapka nocna', 'value': 70, 'weight': 6},
    {'name': 'srebrne sztućce', 'value': 100, 'weight': 1},
    {'name': 'porcelana', 'value': 250, 'weight': 3},
    {'name': 'figura z brązu', 'value': 300, 'weight': 10},
    {'name': 'skórzana torebka', 'value': 280, 'weight': 3},
    {'name': 'zegar', 'value': 300, 'weight': 15}
]

max_weight = 25
chromosome_length = len(items)
mate_rate = 0.5
mutation_rate = 0.2

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("attr_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual,
                 toolbox.attr_bool, chromosome_length)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


def fitness(chromosome):
    weight = 0
    value = 0
    for i in range(chromosome_length):
        if chromosome[i]:
            weight += items[i]['weight']
            value += items[i]['value']

    return [value if weight <= max_weight else 0]


toolbox.register("evaluate", fitness)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)

pop = toolbox.population(n=200)

best = tools.HallOfFame(1)
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("avg", numpy.mean)
stats.register("std", numpy.std)
stats.register("min", numpy.min)
stats.register("max", numpy.max)

pop, log = algorithms.eaSimple(pop, toolbox, cxpb=mate_rate, mutpb=mutation_rate, ngen=40,
                               stats=stats, halloffame=best, verbose=False)

generations = [i['gen'] for i in log]
bests = [i['max'] for i in log]
averages = [i['avg'] for i in log]

fig = go.Figure()
fig.add_trace(go.Scatter(x=tuple(generations),y=tuple(bests),mode='lines+markers',name='Max'))
fig.add_trace(go.Scatter(x=tuple(generations),y=tuple(averages),mode='lines+markers',name='Avg'))
fig.update_layout(
    title = "Problem plecakowy",
    xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text="Generacje")),
    yaxis=go.layout.YAxis(title=go.layout.yaxis.Title(text="Wartość")),
)
fig.show()
