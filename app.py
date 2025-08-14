from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from the form
        time = float(request.form['time'])
        ejection_fraction = float(request.form['ejection_fraction'])
        serum_creatinine = float(request.form['serum_creatinine'])

        # Prepare the input for prediction
        input_features = np.array([[time, ejection_fraction, serum_creatinine]])
        prediction = model.predict(input_features)

        # Return the result
        if prediction[0] == 1:
            result = "The patient is at risk of heart failure."
        else:
            result = "The patient is not at risk of heart failure."

        return render_template('index.html', prediction_text=result)
    except Exception as e:
        return render_template('index.html', prediction_text="Error occurred: " + str(e))

if __name__ == '__main__':
    app.run(debug=True)

