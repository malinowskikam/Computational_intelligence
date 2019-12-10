import pandas
from keras.layers import Dense
from neural import NeuralNetwork
import plotly.graph_objects as go
from diabetes_classifiers import names,scores


def parse_class(name):
    if name == "tested_positive":
        return 1, 0
    elif name == "tested_negative":
        return 0, 1
    else:
        raise ValueError


nn = NeuralNetwork()\
    .add_layer(Dense(10, input_shape=(8,), activation='relu', name='fc1'))\
    .add_layer(Dense(10, activation='relu', name='fc2'))\
    .add_layer(Dense(2, activation='softmax', name='output'))\
    .compile()

dataframe = pandas.read_csv("diabetes.csv")

positive = list()
negative = list()

for index, row in dataframe.iterrows():
    result = parse_class(row[8])

    positive.append(result[0])
    negative.append(result[1])

dataframe["positive"] = positive
dataframe["negative"] = negative

learning_set = dataframe.sample(frac=0.7)
testing_set = dataframe[~dataframe.isin(learning_set).all(1)]

x = [
    "pregnant-times",
    "glucose-concentr",
    "blood-pressure",
    "skin-thickness",
    "insulin",
    "mass-index",
    "pedigree-func",
    "age"
]
y = ["positive", "negative"]

nn.fit(learning_set[x],learning_set[y],epochs=200,verbose=0,batch_size=5)

nn.evaluate(testing_set[x],testing_set[y])

print()
print(f"AccuracY: {nn.evaluation_result[1]}, Loss: {nn.evaluation_result[0]}")

names.append("neural network")
scores.append(nn.evaluation_result[1])

print()
print("Accuracy comparation:")
for name, score in zip(names, scores):
    print(f"Classifier: {name} - {score}")

fig = go.Figure(data=[
    go.Bar(name="Dokładność", x=names, y=scores),
])
fig.show()