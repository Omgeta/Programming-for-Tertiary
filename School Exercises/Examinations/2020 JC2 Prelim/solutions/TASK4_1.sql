DROP TABLE IF EXISTS Registration;
DROP TABLE IF EXISTS Arts;
DROP TABLE IF EXISTS Cultural;
DROP TABLE IF EXISTS Sports;
CREATE TABLE IF NOT EXISTS Registration (
    StudentID INTEGER,
    Type TEXT,
    Venue TEXT
    Session TEXT,
    PRIMARY KEY (StudentID)
);
CREATE TABLE IF NOT EXISTS Arts (
    StudentID INTEGER,
    Performance TEXT CHECK(Performance in ('True', 'False')),
    PRIMARY KEY (StudentID),
    FOREIGN KEY (StudentID) REFERENCES Registration(StudentID)
);
CREATE TABLE IF NOT EXISTS Cultural (
    StudentID INTEGER,
    Race TEXT,
    PRIMARY KEY (StudentID),
    FOREIGN KEY (StudentID) REFERENCES Registration(StudentID)
);
CREATE TABLE IF NOT EXISTS Sports (
    StudentID INTEGER,
    Contact TEXT CHECK(Contact in ('NC', 'C')),
    Cost REAL,
    PRIMARY KEY (StudentID),
    FOREIGN KEY (StudentID) REFERENCES Registration(StudentID)
);