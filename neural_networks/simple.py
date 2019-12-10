import numpy as np


def fun_act(value):
    return 1.0/(1 + np.exp(-value))


def neu(wiek,waga,wzrost):
    h1 = fun_act(wiek*-0.46122 + waga*0.97314 + wzrost*-0.39203 + 0.80109)
    h2 = fun_act(wiek*0.78548 + waga*2.10584 + wzrost*-0.57847 + 0.43529)

    return h1*-0.81546 + h2*1.03775 - 0.2368


data_v = [
    [23, 75, 176],
    [25, 67, 180],
    [28, 120, 175],
    [22, 65, 165],
    [46, 70, 187],
    [50, 68, 180],
    [48, 97, 178]
]

target_v = [1, 1, 0, 1, 1, 0, 0]

for data,target in zip(data_v,target_v):
    print("Data: " + str(data) + ", pred: " + str(neu(*data)) + ", target: " + str(target))