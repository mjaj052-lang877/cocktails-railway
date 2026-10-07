import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow GitHub Pages to call this API

# HEALTH CHECK - VERIFY SERVER IS ALIVE
@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200

# PURE API ENDPOINT - NO HTML SERVED
@app.route('/api/rsvp', methods=['POST'])
def handle_rsvp():
    try:
        data = request.get_json(silent=True) or {}
        name = data.get('name', 'Guest')
        email = data.get('email', '')
        print(f"RSVP API Received: {name} | {email}")
        
        # TODO: Add DB/email logic here
        
    except Exception as e:
        print(f"API Error: {e}")
    
    # RETURN REDIRECT URL AS JSON - NO HTML RENDERING
    return jsonify({
        "redirect": "https://mjaj052-lang877.github.io/event-rsvp-2024/"
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)
