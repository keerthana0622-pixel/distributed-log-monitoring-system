import os

# Database configuration
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", "your_password"),
    "database": os.getenv("DB_NAME", "log_monitoring")
}

# Application settings
APP_HOST = "127.0.0.1"
APP_PORT = 5000
DEBUG_MODE = True

# Log parsing settings
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Error detection threshold
ERROR_THRESHOLD = 5

# API endpoints (for clients)
BASE_API_URL = "http://127.0.0.1:5000"

LOG_ENDPOINT = f"{BASE_API_URL}/logs"
