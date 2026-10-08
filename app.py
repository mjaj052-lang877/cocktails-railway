import os
from flask import Flask, send_from_directory, jsonify

app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    print(f"STARTING ON PORT {port}", flush=True)
    app.run(host='0.0.0.0', port=port)
