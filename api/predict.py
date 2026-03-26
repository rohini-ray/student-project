import json

def handler(request):
    try:
        data = request.json()
        marks = float(data.get("marks", 0))

        # Your logic here
        result = marks * 2

        return {
            "statusCode": 200,
            "body": json.dumps({"prediction": result})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }