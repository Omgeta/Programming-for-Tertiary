from flask import Flask
from flask import redirect, render_template, request
import sqlite3

def get_conn():
	"""
	Get connection to SQLite DB for schools
	Return:
		conn - Connection object
	"""
	conn = sqlite3.connect("../schools.db")
	conn.row_factory = sqlite3.Row
	return conn

def get_zone(school_name: str) -> str:
	"""
	Get school zone from school
	Param:
		school_name (str) - School to look for
	Return:
		school_zone (str) - School zone found
	"""
	conn = get_conn()
	cur = conn.cursor()
	cur.execute(
		"""
		SELECT *
		FROM School
		WHERE Name = ?;
		""", (school_name, )
	)
	school_zone = cur.fetchone()["Zone"]
	return school_zone
	
def get_subjects(school_name) -> list:
	"""
	Get school subjects from school
	Param:
		school_name (str) - School to look for
	Return:
		school_subjects (list) - List of subjects found
	"""
	conn = get_conn()
	cur = conn.cursor()
	cur.execute(
		"""
		SELECT Subject.Name
		FROM School
		LEFT JOIN Subject ON School.SchoolID = Subject.SchoolID
		WHERE School.Name = ?;
		""", (school_name, )
	)
	school_subjects = [subject[0] for subject in cur.fetchall()]
	return school_subjects


app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")
	
@app.route("/result", methods=["POST"])
def result():
	school_name = request.form["school_name"]
	school_zone = get_zone(school_name)
	school_subjects = get_subjects(school_name)
	
	return render_template("result.html", name=school_name, zone=school_zone, subjects=school_subjects)
	
app.run()