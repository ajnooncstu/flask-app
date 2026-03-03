from flask import Flask, jsonify
import os
import sys
from app.storage import ensure_data_dir

app = Flask(__name__)

DATA_DIR = "/etc/flaskdata"

ensure_data_dir(DATA_DIR)

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/secret")
def secret():
    secret = os.getenv("SECRET_KEY")
    if not secret:
        return jsonify({"error": "SECRET_KEY missing"}), 500
    return jsonify({"secret": secret})

@app.route("/crash")
def crash():
    sys.exit(1)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
