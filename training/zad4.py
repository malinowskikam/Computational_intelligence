import random
import numpy


#a
def losuj(a, b):
    return random.randint(min(a, b), max(a+1, b+1))


print("losuj(5,50): " + str(losuj(5, 50)))


#b
def standaryzuj(v):
    odchylenie = numpy.std(v)
    srednia = numpy.mean(v)

    wektor_standardowy = []

    for x in v:
        wektor_standardowy.append((x-srednia)/odchylenie)

    return wektor_standardowy


v = [0, 2, 5, 10, 9, 1, 4, 2]
print("Wektor v = ", v, ", srednia = ", numpy.mean(v), ", odchylenie = ", numpy.std(v))
v_std = standaryzuj(v)
print("Wektor standardowy = ", v_std, ", srednia = ", numpy.mean(v_std), ", odchylenie = ", numpy.std(v_std))


#c
def normalizuj(v,min_v,max_v,new_min,new_max):
    v_minus_min = numpy.subtract(v, [min_v]*len(v))
    divided_by_range = v_minus_min/(max_v-min_v)
    multiplyed_by_new_range = divided_by_range * (new_max-new_min)
    return list(multiplyed_by_new_range + new_min)


v_norm = normalizuj(v, min(v), max(v), 0, 1)
print("Wektor normalny [0,1] = ", str(v_norm), ", srednia = ", numpy.mean(v_norm), ", odchylenie = ", numpy.std(v_norm))


#d
def wyszukaj(v, x):
    result = []
    for element in v:
        if element>x:
            result.append(element)

    return result


v_search = wyszukaj(v, 3)
print("Wektor wynikowy wyszukaj(v,3) = ", str(v_search), ", srednia = ", numpy.mean(v_search), ", odchylenie = ", numpy.std(v_search))