# Dependencies
import sqlite3
import csv

# Class definitions
class School:
	level = None
	YearsOfStudy = None
	def __init__(self, id: int, name: str, zone: str):
		self.id = id
		self.name = name
		self.zone = zone
		
	def safe_name(self) -> str:
		"""
		Returns a string containing no spaces for use in older systems
		Returns:
			safe_name (str) - Safe name
		"""
		safe_name = self.name.replace(" ", "_")
		for c in ("'", ",", "."):
			safe_name = safe_name.replace(c, "")
		return safe_name
		
	def as_record(self) -> tuple:
		"""
		Returns tuple of instance values in SQL Table Column order
		Returns:
			record (tuple) - Instance data 
		"""
		return (
			self.id,
			self.name,
			self.zone,
			self.level,
			self.YearsOfStudy
		)

		
		
class PrimarySchool(School):
	level = "primary"
	YearsOfStudy = 6
	
	
	
class SecondarySchool(School):
	level = "secondary"
	YearsOfStudy = 5
	

	
class JuniorCollege(School):
	level = "junior college"
	YearsOfStudy = 2
	
	
# Loading Schools
def get_schools():
	'''
	Read school data from school_info.csv
	Return:
		schools (list) - List of school objects
	'''
	schools = []
	level_to_class = {
		"PRIMARY": PrimarySchool,
		"SECONDARY": SecondarySchool,
		"JUNIOR COLLEGE": JuniorCollege
	}
	with open("../school_info.csv", "r") as f:
		reader = csv.DictReader(f)
		for row in reader:
			data = (row["school_id"], row["school_name"], row["zone"])
			SchoolClass = level_to_class[row["level"]]
			schools.append(SchoolClass(*data))
	return schools
			
	
# Databasing
def get_conn():
	conn = sqlite3.connect("schools.db")
	return conn
	
def init_db():
	conn = get_conn()
	cur = conn.cursor()
	
	cur.executescript(
		'''
		DROP TABLE IF EXISTS School;
		DROP TABLE IF EXISTS Subject;
		CREATE TABLE IF NOT EXISTS School (
			SchoolID INTEGER PRIMARY KEY,
			Name TEXT,
			"Zone" TEXT,
			"Level" TEXT,
			YearsOfStudy INTEGER
		);
		CREATE TABLE IF NOT EXISTS Subject (
			SchoolID INTEGER,
			Name TEXT,
			PRIMARY KEY (SchoolID, Name),
			FOREIGN KEY (SchoolID) REFERENCES School(SchoolID)
		);
		'''
	)
	
	conn.commit()
	conn.close()
	
def	insert_schools():
	conn = get_conn()
	cur = conn.cursor()
	schools = get_schools()
	for sch in schools:
		cur.execute(
			"""
			INSERT INTO School (
				SchoolID,
				Name,
				"Zone",
				"Level",
				YearsOfStudy
			) VALUES (?, ?, ?, ?, ?);
			""", sch.as_record()
		)
	conn.commit()
	conn.close()
	
init_db()
insert_schools()
		