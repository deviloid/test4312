from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
	return "Meri Kachuyi!"
    return "Meri pyari Kachuyi! 😘😘😘"