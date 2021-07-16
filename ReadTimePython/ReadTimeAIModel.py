import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
# Import Gaussian Naive Bayes classifier:
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
# Import dataset:
url = "C:/Users/kzenczak/Downloads/data.csv"


# Assign column names to dataset:
names = ['name', 'keyCode', 'timeClick', 'timeNext']

# Convert dataset to a pandas dataframe:
data = pd.read_csv(url)


# Use head() function to return the first 5 rows:


x=data.drop("name",axis=1)
y=np.ravel(data['name'])


print(x)

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.5, random_state=50)

print(x_train)
print(y_train)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler().fit(x_train)

x_train = scaler.transform(x_train)

x_test = scaler.transform(x_test)

from sklearn.svm import SVC
svc_model = SVC()

svc_model.fit(x_train, y_train)

y_predict = svc_model.predict(x_test)


from sklearn.metrics import classification_report, confusion_matrix

# cm = np.array(confusion_matrix(y_test, y_predict, labels=["Krystian","Maciek"]))
#
# confusion = pd.DataFrame(cm, index=['TimeClick', 'TimeNext'], columns=['Predicted Diabetes', 'Predicted Healthy'])
# sns.heatmap(confusion,annot=True,fmt='g')
print(classification_report(y_test, y_predict))