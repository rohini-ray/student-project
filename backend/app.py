from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return "Backend Running ✅"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    study = float(data['study_hours'])
    attendance = float(data['attendance'])
    previous = float(data['previous_marks'])
    sleep = float(data['sleep_hours'])

    features = np.array([[study, attendance, previous, sleep]])

    prediction = model.predict(features)

    return jsonify({
        "predicted_marks": float(prediction[0])
    })

if __name__ == "__main__":
    app.run(debug=True)