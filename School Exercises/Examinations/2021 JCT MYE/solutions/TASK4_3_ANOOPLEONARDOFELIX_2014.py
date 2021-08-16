# Dependencies
import sqlite3
import csv

# Databasing
def get_conn():
	conn = sqlite3.connect("schools.db")
	return conn
	
def insert_subjects():
	conn = get_conn()
	cur = conn.cursor()
	with open("../subjects_offered.csv", "r") as f:
		reader = csv.DictReader(f)
		for row in reader:
			cur.execute(
				"""
				INSERT INTO Subject(
					SchoolID,
					Name
				) VALUES (:school_id, :subject_desc)
				""", row
			)
	conn.commit()
	conn.close()
	
insert_subjects()