import os
from flask import Flask, request, redirect, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

# HEALTH CHECK ROUTE - VERIFY SERVER IS ALIVE
@app.route('/health')
def health():
    return {"status": "ok", "message": "Cocktails & Conversation RSVP Server Running"}, 200

# MAIN LURE PAGE
@app.route('/')
def index():
    # Make sure your original lure HTML is in /templates/index.html
    # OR if serving from static, use: return app.send_static_file('index.html')
    try:
        return render_template('index.html')
    except Exception as e:
        print(f"Template Error: {e}")
        return app.send_static_file('index.html')

# RSVP HANDLER WITH SEAMLESS GITHUB PAGES REDIRECT
@app.route('/rsvp', methods=['POST'])
def handle_rsvp():
    try:
        # Process RSVP data safely
        name = request.form.get('name', 'Guest')
        email = request.form.get('email', '')
        print(f"RSVP Received: {name} | {email}")
        
        # TODO: Add your DB/email logic here
        
    except Exception as e:
        print(f"RSVP Processing Error: {e}")
    
    # ALWAYS REDIRECT TO TRUSTED GITHUB PAGES
    return redirect('https://mjaj052-lang877.github.io/event-rsvp-2024/', code=302)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    print(f"Starting server on port {port}...")
    app.run(host='0.0.0.0', port=port, debug=False)
