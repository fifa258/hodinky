from datetime import datetime

from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def index():
    now = datetime.now()
    # Čas serveru jako epoch (ms) pro přesnou synchronizaci analogového ciferníku
    return render_template("index.html", now=now, epoch_ms=int(now.timestamp() * 1000))


@app.route("/time")
def time_json():
    now = datetime.now()
    return jsonify(
        iso=now.isoformat(timespec="seconds"),
        epoch_ms=int(now.timestamp() * 1000),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
