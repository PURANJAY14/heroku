import numpy as np
from flask import Flask, request, jsonify, render_template,redirect,url_for
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    x=final_features[0][1]
    y=final_features[0][1]
    z=final_features[0][2]
    if x>50 :
        return redirect(url_for('home'))
    if y>10 :
        return redirect(url_for('home'))
    if z>10 :
        return redirect(url_for('home'))
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)