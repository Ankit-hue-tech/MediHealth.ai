function fillExample(text) {
    document.getElementById("message").value = text;
}

async function analyzeMessage() {
    const message = document.getElementById("message").value;

    if (!message.trim()) {
        alert("Please enter a message");
        return;
    }

    const response = await fetch("/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
    });

    const data = await response.json();

    document.getElementById("verdict").innerText = data.verdict;
    document.getElementById("risk").innerText = data.risk + "%";
    document.getElementById("reason").innerText = data.reason;
    document.getElementById("suggestion").innerText =
        "✔ Trusted Advice: " + data.suggestion;
}
