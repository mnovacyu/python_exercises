from sklearn import tree

# Dataset
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]

# Label
fruits = {
    0: "orange",
    1: "apple"}

# Train a classifier with decision tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

# Predict fruit output based on input
while True:
    weight = input("Weight of fruit in grams? ")
    bumpy = input("Bumpy or not? (1/0): ")
    fruit = [weight, bumpy]

    print(fruits[clf.predict([fruit])[0]])
    print()
