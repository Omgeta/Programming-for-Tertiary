from flask import Flask
from flask import render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

app.run("0.0.0.0")