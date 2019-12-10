import pandas
from keras.layers import Dense
from neural import NeuralNetwork
import plotly.graph_objects as go

dataframe = pandas.read_csv("polynomial.csv")

nn = NeuralNetwork()\
    .add_layer(Dense(10, input_shape=(1,), activation='relu', name='fc1'))\
    .add_layer(Dense(10, activation='relu', name='fc2'))\
    .add_layer(Dense(10, activation='relu', name='fc3'))\
    .add_layer(Dense(1, name='output'))\
    .compile(loss='mean_squared_error')\
    .fit(dataframe["x"].values.reshape(-1, 1), dataframe["y"].values.reshape(-1, 1), batch_size=10, epochs=200)

y_nn = nn.predict(dataframe["x"].values.reshape(-1, 1))

fig = go.Figure(data=[
    go.Scatter(name="𝑥^3+3𝑥^2−5𝑥+7", x=dataframe["x"], y=dataframe["y"]),
    go.Scatter(name="neural network", x=dataframe["x"], y=y_nn.reshape(-1))
])

fig.show()