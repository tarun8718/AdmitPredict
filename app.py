from tokenize import Double
import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('Model/new_model.pkl', 'rb'))

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    form_vals = [float(x) for x in request.form.values()]
    #int_features=[9.54,334,116,1,4]
    print("Hello *****", form_vals)
    final_features = [np.array(form_vals)]
    prediction = model.predict(final_features)
    output = prediction[0]*100
    if round(output[0],2) < 80:
        return render_template('index.html', prediction_text="Your chances are {}% <br>• Your chances of getting into that university are pretty low. <br> • You might consider taking your GRE and TOEFL tests once agian. <br> • Rewrite your SOPs and LORs for better chances of admit.<br> • Don't loose hope, All the best! ☺".format(round(output[0],2)))
    else:
        return render_template('index.html', prediction_text="Your chances are {}% <br>• Your chances of getting into that university are pretty high!<br>•All the best! ☺".format(round(output[0],2)))

@app.route('/table')
def table():
    return render_template('index2.html')

if __name__ == "__main__":
    app.run(host="localhost",port=5000,debug=True)