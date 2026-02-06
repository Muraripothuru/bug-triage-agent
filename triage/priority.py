def classify_priority(bug):
    text = (
        bug.get("title", "") +
        bug.get("description", "") +
        " ".join(bug.get("comments", []))
    ).lower()

    confidence = 0.6

    if any(word in text for word in ["crash", "500", "security", "jwt", "sql", "xss"]):
        return "High", 0.9

    if any(word in text for word in ["error", "failed", "not working"]):
        return "Medium", 0.75

    return "Low", confidence
