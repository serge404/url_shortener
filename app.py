from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Setting up Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return "Index page for URL app"

if __name__ == "__main__":
    app.run(debug=True)