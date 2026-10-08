import os
from flask import Flask, request, redirect, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

# HEALTH CHECK - VERIFY SERVER IS ALIVE
@app.route('/health')
def health():
    return jsonify({"status": "ok", "message": "Cocktails & Conversation RSVP Server Running"}), 200

# MAIN LURE PAGE (Your original invitation form)
@app.route('/')
def index():
    return render_template('lure.html')  # Your original RSVP form HTML

# VIDEO-MATCHED CONFIRMATION PAGE
@app.route('/confirm')
def confirm():
    return render_template('confirm.html')

# SILENT API HANDLER FOR BACKGROUND SYNC
@app.route('/api/rsvp', methods=['POST'])
def handle_rsvp():
    try:
        data = request.get_json(silent=True) or {}
        name = data.get('name', 'Guest')
        email = data.get('email', '')
        print(f"RSVP API Received: {name} | {email}")
        
        # TODO: Add your DB/email logic here
        
    except Exception as e:
        print(f"API Error: {e}")
    
    # RETURN REDIRECT URL FOR CLIENT-SIDE HANDLING
    return jsonify({
        "redirect": "/confirm"
    }), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    print(f"Starting server on port {port}...")
    app.run(host='0.0.0.0', port=port, debug=False)
