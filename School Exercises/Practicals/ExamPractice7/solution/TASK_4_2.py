import sqlite3


def get_conn():
    conn = sqlite3.connect("records.db")
    return conn


def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.executescript(
        """
        DROP TABLE IF EXISTS Employee;
        DROP TABLE IF EXISTS Sales;
        DROP TABLE IF EXISTS Tech_support;
        CREATE TABLE Employee(
            Employee_ID INTEGER PRIMARY KEY,
            Employee_name TEXT,
            Job_type TEXT,
            Date_of_employment TEXT,
            Service_status TEXT
        );
        CREATE TABLE Sales(
            id INTEGER PRIMARY KEY,
            Employee_ID INTEGER,
            Total_sales REAL,
            FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID)
        );
        CREATE TABLE Tech_support(
            id INTEGER PRIMARY KEY,
            Employee_ID INTEGER,
            Bugs_resolved INTEGER,
            FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID)
        );
        """
    )
    conn.commit()
    conn.close()


def build_db():
    conn = get_conn()
    cur = conn.cursor()
    # Sales department
    with open("../SALES.txt", "r") as f:
        for line in f:
            data = line.rstrip("\n").split(",")
            record = {
                "Employee_ID": int(data[0]),
                "Employee_name": data[1],
                "Date_of_employment": data[2],
                "Service_status": data[3],
                "Total_sales": float(data[4])
            }

            cur.execute(
                """
                INSERT INTO Employee(
                    Employee_ID,
                    Employee_name,
                    Job_type,
                    Date_of_employment,
                    Service_status
                ) VALUES(?, ?, 'Sales', ?, ?)
                """, (record["Employee_ID"], record["Employee_name"], record["Date_of_employment"], record["Service_status"])
            )
            cur.execute(
                """
                INSERT INTO Sales(
                    Employee_ID,
                    Total_sales
                ) VALUES(?, ?)
                """, (record["Employee_ID"], record["Total_sales"])
            )

    # Tech department
    with open("../TECH_SUPPORT.txt", "r") as f:
        for line in f:
            data = line.rstrip("\n").split(",")
            record = {
                "Employee_ID": int(data[0]),
                "Employee_name": data[1],
                "Date_of_employment": data[2],
                "Service_status": data[3],
                "Bugs_resolved": int(data[4])
            }

            cur.execute(
                """
                INSERT INTO Employee(
                    Employee_ID,
                    Employee_name,
                    Job_type,
                    Date_of_employment,
                    Service_status
                ) VALUES(?, ?, 'Tech_support', ?, ?)
                """, (record["Employee_ID"], record["Employee_name"], record["Date_of_employment"], record["Service_status"])
            )
            cur.execute(
                """
                INSERT INTO Tech_support(
                    Employee_ID,
                    Bugs_resolved
                ) VALUES(?, ?)
                """, (record["Employee_ID"], record["Bugs_resolved"])
            )

    conn.commit()
    conn.close()


init_db()
build_db()
