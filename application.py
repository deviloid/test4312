from flask import Flask, render_template, url_for
from flask_sqlaalchemy import flask_sqlaalchemy
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hostingstart.html')

if __name__ == "__main__":
    app.run(debug=True)