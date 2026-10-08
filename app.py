import os
from flask import Flask, send_from_directory

# INITIALIZE FLASK WITH EXISTING STATIC FOLDER
app = Flask(__name__, static_folder='static', static_url_path='/static')

# SERVE MAIN LURE PAGE AT ROOT
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

# START SERVER ON RAILWAY PORT
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
