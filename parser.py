import re
from datetime import datetime

# Supported log levels
LOG_LEVELS = {"INFO", "ERROR", "WARN", "DEBUG"}

# Regex to parse structured log lines
LOG_PATTERN = re.compile(
    r'^(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s+'
    r'(?P<level>INFO|ERROR|WARN|DEBUG)\s+'
    r'(?P<service>[a-zA-Z0-9_\-]+)\s+'
    r'(?P<message>.*)$'
)


def parse_log_line(log_line):
    """
    Parses a single log line into structured dictionary.
    Returns None if the log format is invalid.
    """
    if not log_line or not isinstance(log_line, str):
        return None

    log_line = log_line.strip()
    match = LOG_PATTERN.match(log_line)

    if not match:
        return None

    data = match.groupdict()

    # Normalize and validate level
    level = data.get("level")
    if level not in LOG_LEVELS:
        return None

    # Convert timestamp to datetime object
    try:
        data["timestamp"] = datetime.strptime(
            data["timestamp"], "%Y-%m-%d %H:%M:%S"
        )
    except ValueError:
        return None

    return data


def parse_logs(log_lines):
    """
    Parses multiple log lines.
    Input: iterable of log lines (list/file lines)
    Output: list of structured log dictionaries
    """
    parsed_logs = []

    for line in log_lines:
        parsed = parse_log_line(line)
        if parsed:
            parsed_logs.append(parsed)

    return parsed_logs
