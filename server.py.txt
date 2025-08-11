from flask import Flask, send_file, request
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route('/tracker.png')
def tracker():
    client_ip = request.remote_addr
    logging.info(f"訪問者 IP: {client_ip}")
    return send_file("tracker.png", mimetype="image/png")

@app.route('/')
def home():
    return "IP Tracker is running."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
