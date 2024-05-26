from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask('__name__')
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    google_analytics_id = os.getenv('GOOGLE_ANALYTICS_ID')
    return render_template('index.html', google_analytics_id=google_analytics_id)

@app.route('/predict', methods=["POST"])
def predict():
    google_analytics_id = os.getenv('GOOGLE_ANALYTICS_ID')
    feature = [int(x) for x in request.form.values()]
    feature_final = np.array(feature).reshape(-1, 1)
    prediction = model.predict(feature_final)
    return render_template('index.html', google_analytics_id=google_analytics_id, prediction_text='Price of House will be Rs. {}'.format(int(prediction)))

if __name__ == '__main__':
    app.run(debug=True)

