import sqlite3

conn = sqlite3.connect("terriblesql.db")
conn.row_factory = sqlite3.Row
cur = conn.cursor()

part1 = cur.execute(
    '''
    SELECT * 
    FROM users 
    WHERE name LIKE "She%"
    ORDER BY age DESC;
    '''
).fetchone()["Name"].split(" ")[0][-3:]

part2 = cur.execute(
    '''
    SELECT *
    FROM users
    WHERE name LIKE "%bert%"
    AND age = 17;
    '''
).fetchone()["Name"][-3:]

part3 = cur.execute(
    '''
    SELECT *
    FROM users
    WHERE name LIKE "% Gil%"
    AND hex(name) LIKE "%656C6%"
    AND length(name) = 14;
    '''
).fetchone()["Name"][-4:]

flag = "CTFSG{" + part1 + part2 + part3 + "}"
print(flag)