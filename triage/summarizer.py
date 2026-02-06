def summarize_issue(bug):
    title = bug.get("title", "")
    description = bug.get("description", "")
    comments = bug.get("comments", [])

    summary = title

    if description:
        summary += " - " + description[:80]

    if comments:
        summary += " | Key note: " + comments[0]

    return summary

