from sklearn import tree
from sklearn.metrics import confusion_matrix
import pandas
import graphviz


dataframe = pandas.read_csv("iris.csv")
feature_names = list(dataframe.drop('irisclass', axis=1).columns)
class_names = [x for x in list(dataframe['irisclass'].unique())]
class_column = 'irisclass'

print("{}\n".format(class_names))

#Full dataframe
decision_tree = tree.DecisionTreeClassifier()
decision_tree.fit(dataframe.drop(class_column, axis=1), dataframe[class_column])

dot_data = tree.export_graphviz(
    decision_tree,
    out_file=None,
    feature_names=feature_names,
    class_names=class_names,
    filled=True,
    proportion=True)
graph = graphviz.Source(dot_data)

graph.render("img_iris_full", cleanup=True, view=False)
print(tree.export_text(decision_tree, feature_names=feature_names))
print("score: {}".format(decision_tree.score(dataframe.drop(class_column, axis=1), dataframe[class_column])))
print("Confusion matrix, n={}".format(len(dataframe.index)))
print(confusion_matrix(dataframe[class_column],decision_tree.predict(dataframe.drop(class_column, axis=1))))
