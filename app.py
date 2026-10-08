import os
from flask import Flask, send_from_directory

# Standard Flask initialization - NO FACTORY PATTERN
app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/health')
def health():
    return {"status": "ok"}, 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    print(f"✅ Starting on port {port}", flush=True)
    app.run(host='0.0.0.0', port=port, debug=False)
