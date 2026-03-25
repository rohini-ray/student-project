async function predict() {

    const data = {
        study_hours: document.getElementById("study").value,
        attendance: document.getElementById("attendance").value,
        previous_marks: document.getElementById("previous").value,
        sleep_hours: document.getElementById("sleep").value
    };

    try {
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        document.getElementById("result").innerText =
            "Predicted Marks: " + result.predicted_marks;

    } catch (error) {
        document.getElementById("result").innerText =
            "❌ Error connecting to backend";
    }
}