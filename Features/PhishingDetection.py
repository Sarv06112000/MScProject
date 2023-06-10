from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from Features.FeaturesExtraction import FeaturesExtraction
import pandas as pd
import numpy as np


def isPhising(url):
    dataset = pd.read_csv('Features/PhishingDataset.csv')
    x = dataset.iloc[:, 1:-1].values
    y = dataset.iloc[:, -1].values
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    clf = RandomForestClassifier(criterion='gini', random_state=1, n_estimators=5, n_jobs=2)
    clf.fit(x_train, y_train)
    y_pred = clf.predict(x_test)
    a = accuracy_score(y_test, y_pred)
    print("Accuracy of Model: ", a)
    # url = input("Enter URL: ")
    feat = FeaturesExtraction(url)
    feature = np.array([feat.getFeatures()])
    y_pred_independent_data = clf.predict(feature)

    # getting co-ordinates training_accuracy vs test_accuracy
    training_accuracy = []
    test_accuracy = []
    # try max_depth from 1 to 50
    depth = range(1, 50)
    for n in depth:
        forest_test = RandomForestClassifier(n_estimators=n)
        forest_test.fit(x_train, y_train)
        # record training set accuracy
        training_accuracy.append(forest_test.score(x_train, y_train))
        # record generalization accuracy
        test_accuracy.append(forest_test.score(x_test, y_test))

    if y_pred_independent_data == -1:
        return True, test_accuracy, training_accuracy
    else:
        return False, test_accuracy, training_accuracy

