from flask import Flask, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
import random, string

# Setting up Flask app
app = Flask(__name__)

# Setting up SQLAlchemy to use SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
db = SQLAlchemy(app)

# Define URL Model
class URL(db.Model):
    # Unique ID for each URL mapping
    id = db.Column(db.Integer, primary_key=True)
    # Each short URL should have a max of 8 chars
    short_url = db.Column(db.String(8), unique=True, nullable=False)
    # Maximum URL length supported by most browsers
    original_url = db.Column(db.String(2048), nullable=False) 

# Function to create the short key for the long URL 
def create_short_url_key(length=8):
    # The possible characters that can be used in the key
    chars = string.ascii_letters + string.digits
    
    # Create the key by picking random chars until length is reached
    key = ""
    for i in range(length):
        key += random.choice(chars)
    return key

@app.route('/')
def index():
    return "Index page for URL app"

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.json
    long_url = data.get('url')

    # Returns a 400 Error if URL is not provided
    if not long_url:
        return jsonify({"error": "URL not provided"}), 400
    
    # Create short key
    short_key = create_short_url_key()
    # Checks if the short key is unique and creates a new one if not
    exisitng_url = URL.query.filter_by(short_url=short_key).first()
    if exisitng_url:
        short_key = create_short_url_key()

    # Add and saves new entry to database
    new_url = URL(short_url=short_key,original_url=long_url)
    db.session.add(new_url)
    db.session.commit()

    # Return shortened URL
    return jsonify(short_url = f"http://127.0.0.1:5000/{short_key}")

@app.route('/<short_key>', methods=['GET'])
def redirect_short_url(short_key):
    # Look through database to find the matching original url using the short key
    url = URL.query.filter_by(short_url=short_key).first()
    
     # If short key is found, user is redirected to the orginal longer url
    if url:
        return redirect(url.original_url)
    
    # If short key isn't found, error message pops up
    if not url:
        return jsonify({"error": "URL not found"}), 404

if __name__ == "__main__":
    # Creating URL database table before any request is processed
    with app.app_context():
        db.create_all()
    app.run(debug=True)