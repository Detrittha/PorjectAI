function predictText() {
    var inputText = document.getElementById("inputText").value;

    fetch("http://localhost:8080/api/process/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: inputText })
    })
    .then(response => response.json())
    .then(data => {
        var predictionElement = document.getElementById("prediction");
        predictionElement.innerText = data.prediction_from_container1;
    })
    .catch(error => {
        console.error("Error occurred: ", error);
    });
}
