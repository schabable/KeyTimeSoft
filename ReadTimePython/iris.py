import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
import time


data = pd.read_csv('C:/Users/kzenczak/Downloads/3000/wspolny_6000.csv')
data.shape        #rows, cols

data.pop('ID')
X=data.drop('name',axis=1)

y=data['name']
names = {'Krystian' : 0, 'Kinga' : 1, 'Patryk' : 2, 'Maciek' : 3}
y = y.apply(lambda x: names[x])
y

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, shuffle=True)


model = RandomForestClassifier(n_estimators=400)

model.fit(X_train,y_train)
score = model.score(X_train, y_train)
print("Score dla train: ", score)
score = model.score(X_test, y_test)
print("Score dla test: ", score)


newTest = pd.read_csv('C:/Users/kzenczak/Downloads/500/kinga_500.csv'  ) #   , delimiter=","
newTest.pop('ID')
newX=newTest.drop('name',axis=1) #login , name
#newX=newTest.drop('name',axis=1) #login , name
newX

newY=newTest['name']
#newY=newTest['name']
newY


newY = newY.apply(lambda x: names[x])
newY

y_pred = model.predict(newX)
y_pred.size
y_pred

print(newX.shape)
print(newY.shape)

score = model.score(newX, newY)
print("Score: ", score)



model=ga