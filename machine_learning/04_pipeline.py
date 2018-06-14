# Import a dataset
from sklearn import datasets
iris = datasets.load_iris()

X = iris.data # features
y = iris.target # labels

# Partition dataset into two sets: train and test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)

# Create classifier
from sklearn import tree
my_classifier = tree.DecisionTreeClassifier()

# Train the classifier
my_classifier.fit(X_train, y_train)

# Test the classifier
predictions = my_classifier.predict(X_test)
print(predictions)

# Calculate accuracy - compare classifier predictions to true results
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))
