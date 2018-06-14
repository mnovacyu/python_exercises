# This exercise is for visualizing a decision tree
import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree

iris = load_iris()

test_idx = [0,50,100]

# Training data
train_target = np.delete(iris.target, test_idx) # data labels
train_data = np.delete(iris.data, test_idx, axis=0)

# Testing data
test_target = iris.target[test_idx] # data labels
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print(test_target) # testing data labels
print(clf.predict(test_data)) # our classifier's prediction of the test data!

# Vizualize the classifier's decision tree
from sklearn.externals.six import StringIO
import pydotplus
dot_data = StringIO()
tree.export_graphviz(
    clf,
    out_file = dot_data,
    feature_names = iris.feature_names,
    class_names = iris.target_names,
    filled = True, rounded = True,
    impurity = False
    )

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("02_iris.pdf")
