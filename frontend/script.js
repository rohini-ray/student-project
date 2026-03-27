async function predictMarks() {
    const hours = document.getElementById("hours").value;

    try {
        const response = await fetch("/api/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ hours: hours })
        });

        const data = await response.json();

        document.getElementById("result").innerText =
            "Predicted Marks: " + data.prediction;

    } catch (error) {
        console.error("Error:", error);
        document.getElementById("result").innerText =
            "❌ Error connecting backend";
    }
}

