def route_bug(bug):
    text = (
        bug.get("title", "") +
        bug.get("description", "")
    ).lower()

    if any(word in text for word in ["xss", "jwt", "sql injection", "csrf"]):
        return "Security"

    if any(word in text for word in ["sql", "database", "db"]):
        return "Database"

    if any(word in text for word in ["api", "auth", "backend", "server"]):
        return "Backend"

    if any(word in text for word in ["ui", "css", "button", "layout"]):
        return "Frontend"

    return "General"

