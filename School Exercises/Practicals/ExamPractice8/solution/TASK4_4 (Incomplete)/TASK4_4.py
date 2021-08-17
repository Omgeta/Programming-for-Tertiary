from flask import Flask
from flask import redirect, render_template
import sqlite3


def get_conn():
    conn = sqlite3.connect("../computercompany.db")
    conn.row_factory = sqlite3.Row
    return conn


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result")
def result():
