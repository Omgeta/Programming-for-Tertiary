CREATE TABLE Employee (
  Employee_ID INTEGER PRIMARY KEY,
  Employee_name TEXT,
  Job_type TEXT,
  Date_of_employment TEXT,
  Service_status TEXT
);
CREATE TABLE Sales (
  id INTEGER PRIMARY KEY,
  Employee_ID INTEGER,
  Total_sales REAL,
  FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID)
);
CREATE TABLE Tech_support (
  id INTEGER PRIMARY KEY,
  Employee_ID INTEGER,
  Bugs_resolved INTEGER,
  FOREIGN KEY (Employee_ID) REFERENCES Employee(Employee_ID)
);
