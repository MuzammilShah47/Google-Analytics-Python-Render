from flask import Flask,render_template,request
import pickle
import numpy as np
import requests

payload = {
    'v': 1,
    'tid': 'G-2KQHVE1M1J',  # Replace with your Tracking ID
    'cid': '555',  # Client ID, can be a unique identifier for your users
    't': 'pageview',
    'dp': '/home',  # Page path
}

response = requests.post("http://www.google-analytics.com/collect", data=payload)

if response.ok:
    print('Event sent successfully')
else:
    print('Failed to send event')

app = Flask('__name__')
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=["POST"])
def predict():
    feature=[int(x) for x in request.form.values()]
    feature_final=np.array(feature).reshape(-1,1)
    prediction=model.predict(feature_final)
    return render_template('index.html',prediction_text='Price of House will be Rs. {}'.format(int(prediction)))

if(__name__=='__main__'):
    app.run(debug=True)

