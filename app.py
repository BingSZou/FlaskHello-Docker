from flask import Flask
from datetime import datetime
from flask import render_template
import re

app = Flask(__name__)

@app.route("/")
def myFunc():
    return "Hello, Flask!!"

@app.route("/hello/<name>")
def hello_name(name: str):

    return render_template("hello.html",
            name=name,
            date=datetime.now() 
        )