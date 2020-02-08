from flask import Flask
from flask import render_template
from flask import request
from app_controller import user_controller
from os import listdir
from os.path import isfile, join
import glob

app = Flask(__name__)

@app.route("/home")
def hello():

    return render_template("hostingstart.html")
    # return "Meri pyari Kachuyi! 😘😘😘"