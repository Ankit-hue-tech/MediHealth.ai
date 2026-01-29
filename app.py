from flask import Flask, render_template, request, jsonify
from detector import analyze_claim

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    message = data.get("message", "")

    result = analyze_claim(message)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
