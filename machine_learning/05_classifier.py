# This builds off of exercise 04_pipeline, but instead of
# using K-nearest Neighbors (KNN), we will write our own classifer.
    # Pros of KNN: Relatively simple
    # Cons of KNN:
        # Computationally intensive,
        # Hard to represent relationships between features

from scipy.spatial import distance

def euc(a,b):
    return distance.euclidean(a,b)

class ScrappyKNN():
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        predictions = []
        for row in X_test:
            label = self.closest(row)
            predictions.append(label)
        return predictions

    def closest(self, row):
        best_dist = euc(row, self.X_train[0])
        best_index = 0
        for i in range(1, len(self.X_train)):
            dist = euc(row, self.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.y_train[best_index]

# Import a dataset
from sklearn import datasets
iris = datasets.load_iris()

X = iris.data # features
y = iris.target # labels

# Partition dataset into two sets: train and test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)

# Use another classfier - K Nearest Neighbors
# from sklearn.neighbors import KNeighborsClassifier
my_classifier = ScrappyKNN()

# Train the classifier
my_classifier.fit(X_train, y_train)

# Test the classifier
predictions = my_classifier.predict(X_test)
print(predictions)

# Calculate accuracy - compare classifier predictions to true results
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, predictions))
