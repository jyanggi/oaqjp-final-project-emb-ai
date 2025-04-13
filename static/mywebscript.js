let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if(this.status == 200) {
                document.getElementById("system_response").innerHTML = xhttp.responseText;
            } else{
                document.getElementById("system_response").innerHTML = "Invalid text! Please try again!";
            }
        }
    };

    xhttp.open("POST", "/emotionDetector", true); 
    xhttp.setRequestHeader("Content-Type", "application/json");
    const data = JSON.stringify({ text_to_analyze: textToAnalyze });
    xhttp.send(data);
};
