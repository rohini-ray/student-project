from flask import Flask, request, jsonify
from flask_cors import CORS   # ✅ import here

app = Flask(__name__)
CORS(app)   # ✅ write here (just after app creation)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    marks = data['marks']
    result = marks * 2
    return jsonify({'prediction': result})

if __name__ == '__main__':
    app.run() 
