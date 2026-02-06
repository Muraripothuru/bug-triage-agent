import json
from triage.summarizer import summarize_issue
from triage.priority import classify_priority
from triage.router import route_bug


def run_triage(bug):
    summary = summarize_issue(bug)
    priority, confidence = classify_priority(bug)
    team = route_bug(bug)

    return {
        "summary": summary,
        "priority": priority,
        "assigned_team": team,
        "confidence": confidence
    }


if __name__ == "__main__":
    with open("sample_bugs.json", "r") as f:
        bug_data = json.load(f)

    result = run_triage(bug_data)

    print("\n--- Bug Triage Result ---")
    for key, value in result.items():
        print(f"{key}: {value}")

