# Task 4.2
# Author: SAMPLE CODE
# Date: 25/03/2021
# version: 1

import csv, sqlite3

def get_conn():
    conn = sqlite3.connect('records.db')
    return conn

conn = get_conn()
cur = conn.cursor()
cur.execute('''DELETE FROM Employee;''')
cur.execute('''DELETE FROM Sales;''')
cur.execute('''DELETE FROM Tech_support;''')
cur.close()
conn.commit()
conn.close()


with open('TECH_SUPPORT.txt') as f:
    header = [
        'Employee_ID',
        'Employee_name',
        'Date_of_Employment',
        'Service_status',
        'Bugs_resolved',
    ]
    for row in csv.reader(f):
        rec = {}
        for i in range(len(header)):
            rec[header[i]] = row[i]
        
        conn = get_conn()
        cur = conn.cursor()
        sqlcmd = '''
            INSERT INTO Employee(
                Employee_ID,
                Employee_name,
                Job_type,
                Date_of_Employment,
                Service_status
            ) VALUES (?, ?, 'Tech_support', ?, ?);
        '''
        cur.execute(
            sqlcmd,
            (
                rec['Employee_ID'],
                rec['Employee_name'],
                rec['Date_of_Employment'],
                rec['Service_status'],
            )
        )
        sqlcmd = '''
            INSERT INTO Tech_support(
                Employee_ID,
                Bugs_resolved
            ) VALUES (?, ?);
        '''
        cur.execute(
            sqlcmd,
            (
                rec['Employee_ID'],
                rec['Bugs_resolved'],
            )
        )
        conn.commit()
        cur.close()
        conn.close()
    

with open('SALES.txt') as f:
    header = [
        'Employee_ID',
        'Employee_name',
        'Date_of_Employment',
        'Service_status',
        'Total_sales',
    ]
    for row in csv.reader(f):
        rec = {}
        for i in range(len(header)):
            rec[header[i]] = row[i]

        conn = get_conn()
        cur = conn.cursor()
        sqlcmd = '''
            INSERT INTO Employee(
                Employee_ID,
                Employee_name,
                Job_type,
                Date_of_Employment,
                Service_status
            ) VALUES (?, ?, 'Sales', ?, ?);
        '''
        cur.execute(
            sqlcmd,
            (
                rec['Employee_ID'],
                rec['Employee_name'],
                rec['Date_of_Employment'],
                rec['Service_status'],
            )
        )
        sqlcmd = '''
            INSERT INTO Sales(
                Employee_ID,
                Total_sales
            ) VALUES (?, ?);
        '''
        cur.execute(
            sqlcmd,
            (
                rec['Employee_ID'],
                rec['Total_sales'],
            )
        )
        conn.commit()
        cur.close()
        conn.close()
