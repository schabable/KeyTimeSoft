import json
import warnings
import joblib
import numpy as np
import pandas as pd
from flask import Flask, request
from flask_cors import cross_origin

warnings.filterwarnings('ignore')
app = Flask(__name__)


def check(df):
    names = {'0': 'Krystian', '1': 'Kinga', '2': 'Patryk'}
    model = joblib.load("modelkfold.joblib")

    newTest = df

    y_pred = model.predict(newTest)

    osoba = str(np.bincount(y_pred).argmax())
    dane = str(np.bincount(y_pred))
    print("Liczby wystąpień: " + dane)

    osoba = names[osoba]

    return osoba


@app.route('/test', methods=["GET", "POST"])
@cross_origin()
def test():
    if request.method == 'POST':
        data = str(request.json)
        dataj = data.replace("'", "")
        dataj = json.loads(dataj)
        df = pd.json_normalize(dataj)

        send = check(df)
        return send


app.run(debug=False)