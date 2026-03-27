import json

def handler(request):
    try:
        data = request.json()

        study = float(data.get("study_hours", 0))
        attendance = float(data.get("attendance", 0))
        previous = float(data.get("previous_marks", 0))
        sleep = float(data.get("sleep_hours", 0))

        # Simple logic (replace with model later)
        result = (study * 5) + (attendance * 0.2) + (previous * 0.5) + (sleep * 2)

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "predicted_marks": round(result, 2)
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": str(e)})
        }