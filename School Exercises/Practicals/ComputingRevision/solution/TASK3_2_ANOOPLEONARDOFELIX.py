from typing import List, Dict
import csv
import sqlite3

def read_csv(filepath: str) -> List[Dict]:
    """
    Read the contents of a CSV file
    and parse into a list of dictionaries
    containing the headers

    Params:
        filepath (str) - Filepath of CSV file to read from.
    Returns:
        result (list) - List of dictionaries
    """
    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        result = [row for row in reader]
    return result

def get_conn():
    """
    Returns database connection to weather.db
    
    Returns:
        con - DB Connection Object
    """
    conn = sqlite3.connect("weather.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """
    Initialises database tables
    """
    conn = get_conn()
    cur = conn.cursor()

    with open("./TASK3_1_ANOOPLEONARDOFELIX.sql") as f:
        script = f.read()
    cur.executescript(script)
    
    conn.commit()
    conn.close()

def build_db():
    """
    Populates tables of weather.db with data from csv dataset
    """
    conn = get_conn()
    cur = conn.cursor()

    data = read_csv("../combined_data.csv")
    for row in data:
        # Get values from CSV
        year_month = row["month"]
        year, month = year_month.split("-")
        maximum_rainfall_in_a_day = row["maximum_rainfall_in_a_day"]
        no_of_rainy_days = row["no_of_rainy_days"]
        total_rainfall = row["total_rainfall"]
        mean_rh = row["mean_rh"]
        mean_temp = row["mean_temp"]
        
        cur.execute(
            """
            INSERT INTO Temperature (year_month, "year", "month", temperature) VALUES (?, ?, ?, ?);
            """, (year_month, year, month, mean_temp)
        )
        cur.execute(
            """
            INSERT INTO Rain (year_month, "year", "month", total, max_daily, "days") VALUES (?, ?, ?, ?, ?, ?);
            """, (year_month, year, month, total_rainfall, maximum_rainfall_in_a_day, no_of_rainy_days)
        )
        cur.execute(
            """
            INSERT INTO Humidity (year_month, "year", "month", "relative") VALUES (?, ?, ?, ?);
            """, (year_month, year, month, mean_rh)
        )

    conn.commit()
    conn.close()


init_db()
build_db()