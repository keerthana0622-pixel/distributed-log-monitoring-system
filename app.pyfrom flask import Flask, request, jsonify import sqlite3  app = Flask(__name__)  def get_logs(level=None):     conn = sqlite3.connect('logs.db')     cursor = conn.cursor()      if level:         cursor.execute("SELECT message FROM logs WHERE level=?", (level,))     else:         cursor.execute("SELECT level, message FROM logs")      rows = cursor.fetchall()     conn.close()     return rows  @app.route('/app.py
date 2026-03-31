from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def get_logs(level=None):
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()

    if level:
        cursor.execute("SELECT message FROM logs WHERE level=?", (level,))
    else:
        cursor.execute("SELECT level, message FROM logs")

    rows = cursor.fetchall()
    conn.close()
    return rows

@app.route('/logs', methods=['GET'])
def fetch_logs():
    level = request.args.get('level')
    logs = get_logs(level)

    return jsonify({
        "logs": logs
    })

if __name__ == '__main__':
    app.run(debug=True)
