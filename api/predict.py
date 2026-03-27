import json

def handler(request):
    try:
        if request.method != "POST":
            return {
                "statusCode": 405,
                "body": json.dumps({"error": "Only POST allowed"})
            }

        data = request.json

        study = float(data.get("study_hours", 0))
        attendance = float(data.get("attendance", 0))
        previous = float(data.get("previous_marks", 0))
        sleep = float(data.get("sleep_hours", 0))

        result = (study * 5) + (attendance * 0.2) + (previous * 0.5) + (sleep * 2)

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({
                "predicted_marks": round(result, 2)
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }