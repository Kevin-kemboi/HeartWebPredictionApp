# -*- coding: utf-8 -*-
import numpy as np
import pickle
from flask import Flask, request, render_template
from recommendation import get_recommendation

# Load ML model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Create application
app = Flask(__name__)

# Bind home function to URL
@app.route('/')
def home():
    return render_template('HeartDiseaseClassifier.html')

# Bind predict function to URL
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form entries
        features = [float(x) for x in request.form.values()]
        # Convert features to array
        array_features = np.array(features).reshape(1, -1)
        # Predict
        prediction = model.predict(array_features)

        # Determine prediction result
        if prediction[0] == 1:
            result = 'Congratulations! The patient is not likely to have heart disease!'
            heart_failure = False
            recommendations = []
        else:
            result = 'The patient is likely to have heart disease!'
            heart_failure = True
            recommendations = get_recommendation(form_values=request.form)

        return render_template('HeartDiseaseClassifier.html', heart_failure=heart_failure, result=result, recommendations=recommendations)

    except Exception as e:
        return render_template('HeartDiseaseClassifier.html', result=f'Error: {e}')

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
