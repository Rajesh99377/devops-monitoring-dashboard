import time
from flask import Flask, jsonify, send_from_directory
from datetime import datetime, timezone
from pathlib import Path

app = Flask(__name__)
START_TIME = time.monotonic()
FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"


@app.route("/")
def home():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/api")
def api_home():
    return jsonify({
        "application": "DevOps Monitoring Dashboard",
        "message": "Backend is running",
        "status": "UP"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "timestamp": datetime.now(timezone.utc).isoformat()
    })
@app.route("/metrics")
def metrics():
    uptime_seconds = round(time.monotonic() - START_TIME, 2)

    return jsonify({
        "application": "DevOps Monitoring Dashboard",
        "status": "UP",
        "uptime_seconds": uptime_seconds
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

