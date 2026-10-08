import os
from flask import Flask, send_from_directory

# Initialize Flask with explicit static folder
app = Flask(__name__, static_folder='static', static_url_path='/static')

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/health')
def health():
    return {"status": "ok"}, 200

# Explicit WSGI entry point for Gunicorn
def create_app():
    return app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    print(f"✅ Cocktails Railway Frontend starting on port {port}", flush=True)
    app.run(host='0.0.0.0', port=port, debug=False)
