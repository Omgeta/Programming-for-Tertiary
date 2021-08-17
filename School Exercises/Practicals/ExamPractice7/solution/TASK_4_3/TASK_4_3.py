from flask import Flask
from flask import redirect, render_template, request
import sqlite3

app = Flask(__name__)


def get_conn():
    conn = sqlite3.connect("../records.db")
    conn.row_factory = sqlite3.Row
    return conn


def get_statuses(status):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT 
            Employee_name,
            Job_type,
            Date_of_employment,
            Service_status
        FROM Employee
        WHERE Service_Status = ?
        ORDER BY Employee_name ASC;
        """, (status,)
    )
    records = cur.fetchall()
    conn.close()
    return records


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    status_query = request.form['status']
    records = get_statuses(status_query.title())
    print(records)
    return render_template("result.html", records=records)


app.run()
