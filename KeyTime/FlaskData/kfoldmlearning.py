import warnings
from statistics import mean

import joblib
import pandas as pd
import requests
from flask import Flask
from matplotlib import pyplot
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold, cross_val_score, LeaveOneOut

warnings.filterwarnings('ignore')


url = "http://localhost:8080/export"

r = requests.get(url)
with open('C:/Users/kzenczak/IdeaProjects/KeyTime/FlaskData/wspolnedane.csv', 'wb') as f:
    f.write(r.content)

data = pd.read_csv('C:/Users/kzenczak/IdeaProjects/KeyTime/FlaskData/wspolnedane.csv')

data.pop("ID")
X = data.drop('name', axis=1)

y = data['name']

print()
names = {'Krystian': 0, 'Kinga': 1, 'Patryk': 2}
y = y.apply(lambda x: names[x])

kf = KFold(n_splits=12, shuffle=True)
model = RandomForestClassifier(n_estimators=80, min_samples_split=25, min_samples_leaf=6, max_features='log2',
                               max_depth=93, bootstrap=True)

for train_index, test_index in kf.split(X):
    model.fit(
        X.values[train_index],
        y.values[train_index])

joblib.dump(model, 'modelkfold.joblib')

##TESTOWANIE
# def get_dataset():
#     url = "http://localhost:8080/export"
#
#     r = requests.get(url)
#     with open('C:/Users/kzenczak/IdeaProjects/KeyTime/FlaskData/wspolnedane.csv', 'wb') as f:
#         f.write(r.content)
#
#     data = pd.read_csv('C:/Users/kzenczak/IdeaProjects/KeyTime/FlaskData/wspolnedane.csv')
#
#     data.pop("ID")
#     X = data.drop('name', axis=1)
#
#     y = data['name']
#
#     print()
#     names = {'Krystian': 0, 'Kinga': 1, 'Patryk': 2}
#     y = y.apply(lambda x: names[x])
#     return X, y
#
#
# def get_model():
#     model = RandomForestClassifier(n_estimators=80, min_samples_split=25, min_samples_leaf=6, max_features='log2',
#                                    max_depth=93, bootstrap=True)
#     return model
#
#
# def evaluate_model(cv):
#     # get the dataset
#     X, y = get_dataset()
#     # get the model
#     model = get_model()
#     # evaluate the model
#     scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1)
#     # return scores
#     return mean(scores), scores.min(), scores.max()
#
#
# ideal, _, _ = evaluate_model(LeaveOneOut())
# print('Ideal: %.3f' % ideal)
#
# # define folds to test
# folds = range(2, 31)
#
# # record mean and min/max of each set of results
# means, mins, maxs = list(), list(), list()
# # evaluate each k value
# for k in folds:
#     # define the test condition
#     cv = KFold(n_splits=k, shuffle=True, random_state=1)
#     # evaluate k value
#     k_mean, k_min, k_max = evaluate_model(cv)
#     # report performance
#     print('> folds=%d, accuracy=%.3f (%.3f,%.3f)' % (k, k_mean, k_min, k_max))
#     # store mean accuracy
#     means.append(k_mean)
#     # store min and max relative to the mean
#     mins.append(k_mean - k_min)
#     maxs.append(k_max - k_mean)
#
#     # line plot of k mean values with min/max error bars
# pyplot.errorbar(folds, means, yerr=[mins, maxs], fmt='o')
# # plot the ideal case in a separate color
# pyplot.plot(folds, [ideal for _ in range(len(folds))], color='r')
# # show the plot
# pyplot.show()
