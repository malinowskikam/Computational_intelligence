import pandas
from keras.layers import Dense
from neural import NeuralNetwork


def parse_class(name):
    if name == "Iris-setosa":
        return 1, 0, 0
    elif name == "Iris-versicolor":
        return 0, 1, 0
    elif name == "Iris-virginica":
        return 0, 0, 1
    else:
        raise ValueError


nn = NeuralNetwork()\
    .add_layer(Dense(10, input_shape=(4,), activation='relu', name='fc1'))\
    .add_layer(Dense(10, activation='relu', name='fc2'))\
    .add_layer(Dense(3, activation='softmax', name='output'))\
    .compile()

dataframe = pandas.read_csv("iris.csv")

setosa = list()
versicolor = list()
virginica = list()

for index, row in dataframe.iterrows():
    result = parse_class(row[4])

    setosa.append(result[0])
    versicolor.append(result[1])
    virginica.append(result[2])

dataframe["setosa"] = setosa
dataframe["versicolor"] = versicolor
dataframe["virginica"] = virginica

print(dataframe)

learning_set = dataframe.sample(frac=0.7)
testing_set = dataframe[~dataframe.isin(learning_set).all(1)]

x = ["sepallength","sepalwidth","petallength","petalwidth"]
y = ["setosa","versicolor","virginica"]

nn.fit(learning_set[x],learning_set[y])

nn.evaluate(testing_set[x],testing_set[y])

print()
print(f"Accuracu: {nn.evaluation_result[1]}, Loss: {nn.evaluation_result[0]}")



