import sqlite3

conn = sqlite3.connect("example.db")
cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE Example(
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        salary REAL,
        FOREIGN KEY (id) REFERENCES Table(id)
    )
    """
)

cur.execute(
    """
    INSERT INTO Example (name, age, salary)
    VALUES (?, ?, ?)
    """, ("Hames", 2, 13.1)
)

cur.execute(
    """
    SELECT * FROM Example WHERE id = ? ORDER BY name ASC
    """, (1, )
)
data = cur.fetchone()
data = cur.fetchall()

conn.commit()
conn.close()
