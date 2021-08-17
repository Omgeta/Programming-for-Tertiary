import sqlite3
import csv


def get_conn():
    conn = sqlite3.connect("computercompany.db")
    return conn


def init_db():
    conn = get_conn()
    cur = conn.cursor()

    cur.executescript(
        '''
        CREATE TABLE IF NOT EXISTS Customer (
            CustomerID TEXT PRIMARY KEY,
            CustomerName TEXT,
            Email TEXT,
            Telephone TEXT
        );
        CREATE TABLE IF NOT EXISTS Office (
            OfficeID INTEGER PRIMARY KEY,
            PostalCode TEXT,
            TELEPHONE TEXT
        );
        CREATE TABLE IF NOT EXISTS SalesPerson (
            SalesPersonID INTEGER PRIMARY KEY,
            SalesPersonName TEXT,
            OfficeID INTEGER,
            FOREIGN KEY (OfficeID) REFERENCES Office(OfficeID)
        );
        CREATE TABLE IF NOT EXISTS Sale (
            id INTEGER PRIMARY KEY,
            SalesPersonID INTEGER,
            CustomerID INTEGER,
            SaleDate TEXT,
            Amount INTEGER,
            FOREIGN KEY (SalesPersonID) REFERENCES SalesPerson(SalesPersonID),
            FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID)
        );
        '''
    )

    conn.commit()
    conn.close()


def build_db():
    conn = get_conn()
    cur = conn.cursor()

    with open("../CUSTOMER.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute(
                '''
                INSERT INTO Customer (
                    CustomerID,
                    CustomerName,
                    Email,
                    Telephone
                ) VALUES (:CustomerID, :CustomerName, :Email, :Telephone);
                ''', row
            )

    with open("../OFFICE.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["OfficeID"] = int(row["OfficeID"])
            cur.execute(
                """
                INSERT INTO Office (
                    OfficeID,
                    PostalCode,
                    Telephone
                ) VALUES (:OfficeID, :PostalCode, :Telephone)
                """, row
            )

    with open("../SALESPERSON.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["SalesPersonID"] = int(row["SalesPersonID"])
            cur.execute(
                """
                INSERT INTO SalesPerson (
                    SalesPersonID,
                    SalesPersonName,
                    OfficeID
                ) VALUES (:SalesPersonID, :SalesPersonName, :OfficeID)
                """, row
            )

    with open("../SALE.CSV", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["SalesPersonID"] = int(row["SalesPersonID"])
            row["Amount"] = int(row["Amount"])
            cur.execute(
                """
                INSERT INTO Sale (
                    SalesPersonID,
                    CustomerID,
                    SaleDate,
                    Amount
                ) VALUES (:SalesPersonID, :CustomerID, :SaleDate, :Amount)
                """, row
            )

    conn.commit()
    conn.close()


init_db()
build_db()
