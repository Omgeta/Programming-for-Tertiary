from flask import Flask
from flask import render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def query():
    queryData = request.form['query']
    result = process(queryData)
    return redirect("/results")

@app.route("/results")
def results():
    return render_template("results.html")


app.run("0.0.0.0")