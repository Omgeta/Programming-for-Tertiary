# Task 4.3
# Author: SAMPLE CODE
# Date: 25/03/2021
# version: 1

from flask import Flask, request, render_template
import sqlite3

def get_conn():
    conn = sqlite3.connect('records.db')
    conn.row_factory = sqlite3.Row
    return conn

status_sql = '''
    SELECT Employee_name,
           Job_type,
           Date_of_employment,
           Service_status
    FROM Employee
    WHERE Service_status = ?
    ORDER BY Employee_name DESC;
'''

def get_records(status):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(status_sql, (status,))
    records = cur.fetchall()
    cur.close()
    conn.close()
    return records

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    status = request.form['status']
    data = get_records(status.title())
    return render_template('result.html', data=data)

app.run()
