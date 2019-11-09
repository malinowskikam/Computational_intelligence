from sklearn import tree
from sklearn.metrics import confusion_matrix
import pandas
import graphviz


dataframe = pandas.read_csv("iris.csv")
feature_names = list(dataframe.drop('irisclass', axis=1).columns)
class_names = [x for x in list(dataframe['irisclass'].unique())]
class_column = 'irisclass'

print("{}\n".format(class_names))

# Splited dataframe
learning_set_frac = 0.7

learning_set = dataframe.sample(frac=learning_set_frac)
testing_set = dataframe[~dataframe.isin(learning_set).all(1)]

decision_tree = tree.DecisionTreeClassifier()
decision_tree.fit(learning_set.drop(class_column, axis=1), learning_set[class_column])

dot_data = tree.export_graphviz(
    decision_tree,
    out_file=None,
    feature_names=feature_names,
    class_names=class_names,
    filled=True,
    proportion=True)
graph = graphviz.Source(dot_data)

graph.render("img_iris_split", cleanup=True, view=False)
print(tree.export_text(decision_tree, feature_names=feature_names))
print("score: {}".format(decision_tree.score(testing_set.drop(class_column, axis=1), testing_set[class_column])))
print("Confusion matrix, n={}".format(len(testing_set.index)))
print(confusion_matrix(testing_set[class_column],decision_tree.predict(testing_set.drop(class_column, axis=1))))



