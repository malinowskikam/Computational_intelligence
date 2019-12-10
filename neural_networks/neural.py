import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

from keras.models import Sequential
from keras.optimizers import Adam

# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


class NeuralNetwork:
    def __init__(self):
        self.model = Sequential()
        self.train_history = None
        self.evaluation_result = None

    def add_layer(self, layer):
        self.model.add(layer)
        return self

    def compile(self, optimizer=Adam(lr=0.001), loss='categorical_crossentropy'):
        self.model.compile(optimizer, loss=loss, metrics=['accuracy'])
        return self

    def fit(self, train_x, train_y, epochs=150, verbose=2, batch_size=5):
        self.train_history = self.model.fit(train_x, train_y, verbose=verbose, batch_size=batch_size, epochs=epochs)
        return self

    def evaluate(self, test_x, test_y):
        self.evaluation_result = self.model.evaluate(test_x, test_y)
        return self

    def predict(self, x):
        return self.model.predict(x)
