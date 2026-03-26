import json
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

def handler(request):
    try:
        data = request.json()
        hours = float(data["hours"])
        
        prediction = model.predict([[hours]])

        return {
            "statusCode": 200,
            "body": json.dumps({"prediction": float(prediction[0])})
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }