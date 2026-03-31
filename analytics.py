from database import fetch_logs
from collections import defaultdict


def get_log_level_distribution():
    logs = fetch_logs(limit=1000)

    distribution = {"INFO": 0, "ERROR": 0, "WARN": 0, "DEBUG": 0}

    for log in logs:
        level = log["level"]
        if level in distribution:
            distribution[level] += 1

    return distribution


def get_service_distribution():
    logs = fetch_logs(limit=1000)

    service_count = defaultdict(int)

    for log in logs:
        service = log["service"]
        service_count[service] += 1

    return service_count


def get_top_services(limit=3):
    service_count = get_service_distribution()

    sorted_services = sorted(
        service_count.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_services[:limit]


def get_system_health():
    logs = fetch_logs(limit=1000)

    total_logs = len(logs)
    error_logs = len([log for log in logs if log["level"] == "ERROR"])

    error_rate = (error_logs / total_logs) * 100 if total_logs > 0 else 0

    return {
        "total_logs": total_logs,
        "error_logs": error_logs,
        "error_rate_percent": round(error_rate, 2)
    }


if __name__ == "__main__":
    print("Log Distribution:", get_log_level_distribution())
    print("Top Services:", get_top_services())
    print("System Health:", get_system_health())
