import os
import sys
from flask import Flask, send_from_directory

try:
    # Initialize Flask with explicit static folder path
    app = Flask(__name__, static_folder='static', static_url_path='/static')

    # Serve main page at root
    @app.route('/')
    def index():
        return send_from_directory('static', 'index.html')

    # Explicitly serve HTA file (Flask sometimes blocks unknown extensions)
    @app.route('/static/<path:filename>')
    def serve_static(filename):
        return send_from_directory(app.static_folder, filename)

    if __name__ == '__main__':
        port = int(os.environ.get('PORT', 8080))
        print(f"✅ Server starting on port {port}...", flush=True)
        app.run(host='0.0.0.0', port=port, debug=False)
        
except Exception as e:
    print(f"❌ FATAL ERROR: {e}", flush=True)
    sys.exit(1)
