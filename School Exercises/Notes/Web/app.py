from flask import Flask
from flask import render_template, redirect, request, send_from_directory
import os

UPLOAD_FOLDER = "./static/uploads"

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def root():
    return render_template("index.html")


@app.route("/query", methods=["POST"])
def query():
    queryData = request.form['query']
    process(queryData)

    file = request.files["file"]
    file.save(os.path.join(app.config["UPLOAD_FOLDER"], file.filename))

    return render_template("/results", filename=file.filename)


@app.route("/uploads/<name>")
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


app.run("0.0.0.0")
