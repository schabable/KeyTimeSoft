import warnings

import joblib
import pandas as pd
import requests
import numpy as np
from flask import Flask
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from pprint import pprint
from sklearn.model_selection import RandomizedSearchCV

warnings.filterwarnings('ignore')

app = Flask(__name__)

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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

#model = RandomForestClassifier(n_estimators=40,min_samples_split=15,min_samples_leaf=2,max_features='log2',max_depth=10, criterion='entropy',class_weight='balanced_subsample',bootstrap=True)

model = RandomForestClassifier(n_estimators=80,min_samples_split=25,min_samples_leaf=6,max_features='log2',max_depth=93,bootstrap=True) #1nowy modelnowybest

#model = RandomForestClassifier(n_estimators=1500,min_samples_split=25,min_samples_leaf=4,max_features='sqrt',max_depth=69,bootstrap=True, oob_score=True) #2
#
#model = RandomForestClassifier(n_estimators=1780,min_samples_split=25,min_samples_leaf=4,max_features='sqrt',max_depth=29,bootstrap=True) #1
#
# #model = RandomForestClassifier(n_estimators=200, min_samples_split=10, min_samples_leaf=2, max_features='auto', max_depth=10, bootstrap=True) #3
#
model.fit(X_train, y_train)
score = model.score(X_train, y_train)
print("Score dla train: ", score)
score = model.score(X_test, y_test)
print("Score dla test: ", score)
joblib.dump(model, 'model.joblib')

#
# rf = RandomForestClassifier()
#
# # Look at parameters used by our current forest
# print('Parameters currently in use:\n')
# pprint(rf.get_params())
#
# # Number of trees in random forest
# n_estimators = [int(x) for x in np.linspace(start=20, stop=2000, num=100)]
# # Number of features to consider at every split
# max_features = ['auto', 'sqrt', 'log2']
# # Maximum number of levels in tree
# max_depth = [int(x) for x in np.linspace(1, 100, num=100)]
# max_depth.append(None)
# # Minimum number of samples required to split a node
# min_samples_split = [2, 5, 7, 9, 10, 15, 20, 25, 30, 40, 60, 80, 100, 150, 200]
# # Minimum number of samples required at each leaf node
# min_samples_leaf = [1, 2, 4, 6, 8, 10, 15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200]
# # Method of selecting samples for training each tree
# bootstrap = [True, False]
# # Create the random grid
# random_grid = {'n_estimators': n_estimators,
#                'max_features': max_features,
#                'max_depth': max_depth,
#                'min_samples_split': min_samples_split,
#                'min_samples_leaf': min_samples_leaf,
#                'bootstrap': bootstrap}
# pprint(random_grid)
#
# # Use the random grid to search for best hyperparameters
# # First create the base model to tune
# rf = RandomForestClassifier()
# # Random search of parameters, using 3 fold cross validation,
# # search across 100 different combinations, and use all available cores
# rf_random = RandomizedSearchCV(estimator=rf, param_distributions=random_grid, n_iter=2000, cv=4, verbose=4, n_jobs=-1)
# # Fit the random search model
# rf_random.fit(X_train, y_train)
#
# print(rf_random.best_params_)
# print(rf_random.best_score_)
# print(rf_random.best_estimator_)
