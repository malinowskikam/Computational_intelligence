import pandas


def classificate2(df): #96%
    if df.petalwidth < 0.8:
       return 'Iris-setosa'
    elif 0.8 <= df.petalwidth < 1.8:
        return 'Iris-versicolor'
    else:
        return 'Iris-virginica'


def classificate(df): #93%
    if df.petalwidth < 0.8:
       return 'Iris-setosa'
    else:
        if df.petallength > 5.0:
            return 'Iris-virginica'
        else:
            return 'Iris-versicolor'


def compare2(df):
    return classificate2(df) == df.irisclass


def compare(df):
    return classificate(df) == df.irisclass


dataframe = pandas.read_csv("iris.csv")

print(
    dataframe.apply(compare,axis=1).mean()
)

print(
    dataframe.apply(compare2,axis=1).mean()
)


