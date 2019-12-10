import pandas
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


def knn(training_set, k):
    k_nearest_neighbours = KNeighborsClassifier(n_neighbors=k, metric='euclidean')
    k_nearest_neighbours.fit(training_set.drop("class", axis=1), training_set["class"])
    return k_nearest_neighbours


def tree(training_set):
    decision_tree = DecisionTreeClassifier()
    decision_tree.fit(training_set.drop("class", axis=1), training_set["class"])
    return decision_tree


def bayes(training_set):
    naive_bayes = MultinomialNB()
    naive_bayes.fit(training_set.drop("class", axis=1), training_set["class"])
    return naive_bayes


def get_score(classifier, test_set):
    return classifier.score(test_set.drop("class", axis=1), test_set["class"])


def get_confusion_matrix(classifier, test_set):
    return confusion_matrix(test_set["class"], classifier.predict(test_set.drop("class", axis=1)))


learning_set_frac = 0.67

dataframe = pandas.read_csv("diabetes.csv")

learning_set = dataframe.sample(frac=learning_set_frac)
testing_set = dataframe[~dataframe.isin(learning_set).all(1)]

nn3 = knn(learning_set, 3)
nn5 = knn(learning_set, 5)
nn11 = knn(learning_set, 11)
dt = tree(learning_set)
nb = bayes(learning_set)

names = ["3-nn", "5-nn", "11-nn", "d-tree", "n-b"]
classifiers = [nn3, nn5, nn11, dt, nb]
scores = [get_score(x, testing_set) for x in classifiers]
