import requests
import random
from datetime import datetime

API_URL = "http://127.0.0.1:5000/logs"

SERVICES = ["auth_service", "payment_service", "order_service"]

LOG_LEVELS = ["INFO", "ERROR", "WARN", "DEBUG"]

MESSAGES = [
    "User login successful",
    "User login failed",
    "Payment processed",
    "Payment failed",
    "Order created",
    "Order cancelled"
]


def generate_log():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    level = random.choice(LOG_LEVELS)
    service = random.choice(SERVICES)
    message = random.choice(MESSAGES)

    log = f"{timestamp} {level} {service} {message}"
    return log


def send_log():
    log = generate_log()

    payload = {
        "log": log
    }

    try:
        response = requests.post(API_URL, json=payload)
        print(response.json())
    except Exception as e:
        print("Error sending log:", e)


if __name__ == "__main__":
    # Send multiple logs
    for _ in range(10):
        send_log()
