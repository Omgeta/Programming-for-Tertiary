# Terrible Sequel

# Description
There is one table in the attached sqlite database. You can use sqlitebrowser to open it. The flag consists of three parts.

Part 1
Find all the users whose name starts with "She", order by the age in descending order. First result. Last three characters of first name. e.g. 'Dave Robin' => 'ave'

Part 2
Find all the users whose name contains "bert" and is 17 years old. First result. Last three characters of name.

Part 3
Find the user who:
1. Has a last name starting with "Gil"
2. Has 656C6 in the hex representation of his/her name.
3. Has a full name that totals to 14 characters.
4. Flag is last 4 characters of the name.

Format is: CTFSG{part1part2part3}

## Analysis

Pretty straight forward series of SQLite queries to find the different parts of the flag.

For all parts of the question, knowledge of the LIKE operator is useful to pattern match the names.

part1
```sql
SELECT 
    * 
FROM 
    users 
WHERE 
    name LIKE "She%"
ORDER BY 
    age DESC;
```

part2
```sql
SELECT 
    *
FROM 
    users
WHERE 
    name LIKE "%bert%"
AND 
    age = 17;
```

part3
```sql
SELECT 
    *
FROM 
    users
WHERE 
    name LIKE "% Gil%"
AND 
    hex(name) LIKE "%656C6%"
AND 
    length(name) = 14;
```

## Solution

```py
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
```

Flag obtained is:
```txt
CTFSG{enablemore}
```
