import mysql.connector
from mysql.connector import Error


# Database configuration
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "your_password",
    "database": "log_monitoring"
}


def get_connection():
    """
    Creates and returns a database connection
    """
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print("Database connection error:", e)
        return None


def create_table():
    """
    Creates logs table if it doesn't exist
    """
    connection = get_connection()
    if connection is None:
        return

    cursor = connection.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS logs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        timestamp DATETIME,
        level VARCHAR(10),
        service VARCHAR(100),
        message TEXT
    )
    """

    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()


def insert_log(log_data):
    """
    Inserts a parsed log into the database
    log_data should be a dictionary with keys:
    timestamp, level, service, message
    """
    connection = get_connection()
    if connection is None:
        return False

    cursor = connection.cursor()

    query = """
    INSERT INTO logs (timestamp, level, service, message)
    VALUES (%s, %s, %s, %s)
    """

    values = (
        log_data["timestamp"],
        log_data["level"],
        log_data["service"],
        log_data["message"]
    )

    try:
        cursor.execute(query, values)
        connection.commit()
        return True
    except Error as e:
        print("Insert error:", e)
        return False
    finally:
        cursor.close()
        connection.close()


def fetch_logs(limit=100):
    """
    Fetch recent logs from database
    """
    connection = get_connection()
    if connection is None:
        return []

    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM logs ORDER BY timestamp DESC LIMIT %s"
    cursor.execute(query, (limit,))

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results


def fetch_error_logs():
    """
    Fetch only ERROR logs
    """
    connection = get_connection()
    if connection is None:
        return []

    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM logs WHERE level = 'ERROR' ORDER BY timestamp DESC"
    cursor.execute(query)

    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return results
