from flask import Flask, request, jsonify
from parser import parse_log_line

app = Flask(__name__)

# In-memory storage (replace with DB later)
logs_storage = []


@app.route("/logs", methods=["POST"])
def ingest_log():
    data = request.get_json()

    if not data or "log" not in data:
        return jsonify({"error": "Log data is required"}), 400

    parsed_log = parse_log_line(data["log"])

    if not parsed_log:
        return jsonify({"error": "Invalid log format"}), 400

    logs_storage.append(parsed_log)

    return jsonify({"message": "Log stored successfully"}), 201


@app.route("/logs", methods=["GET"])
def get_logs():
    return jsonify(logs_storage), 200


@app.route("/logs/errors", methods=["GET"])
def get_error_logs():
    error_logs = [log for log in logs_storage if log["level"] == "ERROR"]
    return jsonify(error_logs), 200


if __name__ == "__main__":
    app.run(debug=True)
