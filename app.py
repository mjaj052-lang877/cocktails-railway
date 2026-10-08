import os
from flask import Flask, send_from_directory, request, jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
CORS(app)

@app.route('/')
def index():
    # Your original lure page HTML should be in static/index.html
    return send_from_directory('static', 'index.html')

@app.route('/confirm')
def confirm():
    # Serves the new dark-themed confirmation page from static folder
    return send_from_directory('static', 'confirm.html')

@app.route('/api/rsvp', methods=['POST'])
def handle_rsvp():
    data = request.get_json(silent=True) or {}
    print(f"RSVP Received: {data.get('name', 'Guest')}")
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
