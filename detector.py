def analyze_claim(text):
    text = text.lower()

    risk = 10
    verdict = "Low Risk"
    reasons = []

    fake_keywords = ["miracle", "cure", "cures", "guaranteed", "instant", "pill"]

    for word in fake_keywords:
        if word in text:
            risk += 20
            reasons.append(f"Contains suspicious medical claim: '{word}'")

    if risk >= 60:
        verdict = "High Risk Misinformation"
    elif risk >= 30:
        verdict = "Potentially Misleading"

    suggestion = "Refer to trusted medical sources like WHO or consult a certified doctor."

    return {
        "verdict": verdict,
        "risk": min(risk, 90),
        "reason": " | ".join(reasons) if reasons else "No dangerous patterns detected.",
        "suggestion": suggestion
    }
