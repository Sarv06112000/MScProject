from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from Features.FeaturesExtraction import FeaturesExtraction
import pandas as pd
import numpy as np


def isPhising(url):
    dataset = pd.read_csv('PhishingDataset.csv')
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
    # print(y_pred_independent_data)
    if y_pred_independent_data == -1:
        return False
    else:
        return True

