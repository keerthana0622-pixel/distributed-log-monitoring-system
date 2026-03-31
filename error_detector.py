from database import fetch_logs
from collections import defaultdict


ERROR_THRESHOLD = 5  # configurable threshold


def detect_errors():
    logs = fetch_logs(limit=1000)

    error_count = defaultdict(int)

    for log in logs:
        if log["level"] == "ERROR":
            service = log["service"]
            error_count[service] += 1

    alerts = []

    for service, count in error_count.items():
        if count >= ERROR_THRESHOLD:
            alerts.append({
                "service": service,
                "error_count": count,
                "alert": "High error rate detected"
            })

    return alerts


def get_error_summary():
    logs = fetch_logs(limit=1000)

    summary = defaultdict(lambda: {"INFO": 0, "ERROR": 0, "WARN": 0, "DEBUG": 0})

    for log in logs:
        level = log["level"]
        service = log["service"]
        summary[service][level] += 1

    return summary


if __name__ == "__main__":
    alerts = detect_errors()
    summary = get_error_summary()

    print("ALERTS:", alerts)
    print("SUMMARY:", summary)
