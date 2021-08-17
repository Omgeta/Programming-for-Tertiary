CREATE TABLE IF NOT EXISTS Customer (
    CustomerID TEXT PRIMARY KEY,
    CustomerName TEXT,
    Email TEXT,
    Telephone TEXT,
);
CREATE TABLE IF NOT EXISTS Office (
    OfficeID INTEGER PRIMARY KEY,
    PostalCode TEXT,
    TELEPHONE TEXT,
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