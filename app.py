from flask import Flask
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

if __name__ == "__main__":
    # Creating URL database table before any request is processed
    with app.app_context():
        db.create_all()
    app.run(debug=True)