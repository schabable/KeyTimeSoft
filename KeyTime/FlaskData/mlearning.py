import warnings

import joblib
import pandas as pd
import requests
from flask import Flask
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

warnings.filterwarnings('ignore')

app = Flask(__name__)

url="http://localhost:8080/export"

r = requests.get(url)
with open('C:/Users/kzenczak/IdeaProjects/KeyTime/FlaskData/wspolnedane.csv', 'wb') as f:
    f.write(r.content)

data = pd.read_csv('C:/Users/kzenczak/IdeaProjects/KeyTime/FlaskData/wspolnedane.csv')

data.pop("ID")
X = data.drop('name', axis=1)

y = data['name']
names = {'Krystian': 0, 'Kinga': 1, 'Patryk': 2, 'Maciek': 3}
y = y.apply(lambda x: names[x])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)

model = RandomForestClassifier(n_estimators=500)

model.fit(X_train, y_train)
score = model.score(X_train, y_train)
print("Score dla train: ", score)
score = model.score(X_test, y_test)
print("Score dla test: ", score)
joblib.dump(model, 'model.joblib')