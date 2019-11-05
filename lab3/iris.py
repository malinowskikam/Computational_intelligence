import pandas
import numpy

dataframe = pandas.read_csv("iris_with_errors.csv")
df_num = dataframe.drop('variety', axis=1).apply(pandas.to_numeric,errors='coerce')
df_names = dataframe['variety']

print("null values:\n" + str(
    dataframe
        .isnull()
        .sum()
))
print()

print("not numeric values:\n" + str(
    df_num
        .isnull()
        .sum()
))
print()

print("outside range values:\n" + str(
    df_num
        .where(numpy.logical_and(df_num>0,df_num<=15))
        .isnull()
        .sum()
))
print()

df_median = df_num\
    .where(numpy.logical_and(df_num<=15,df_num>0))\
    .median()


print("median of valid values:\n" + str(df_median))
print()

df_valid = df_num\
        .where(numpy.logical_and(df_num<=15,df_num>0))\
        .fillna(df_median)

print("outside range values in fixed:\n" + str(
    df_valid
        .where(numpy.logical_and(df_valid>0,df_valid<=15))
        .isnull()
        .sum()
))
print()

print("median of all values in fixed:\n" + str(
    df_valid
        .median()
))
print()

print('all unique names in "variety":\n'+ str(
    df_names
        .value_counts()
))
print()

df_names_fixed = df_names\
    .replace('setosa','Setosa')\
    .replace('Versicolour','Versicolor')\
    .replace('virginica','Virginica')

print('all unique names in "variety" (fixed):\n'+ str(
    df_names_fixed
        .value_counts()
))