DROP TABLE IF EXISTS People;
CREATE TABLE IF NOT EXISTS People(
    PersonID INTEGER AUTOINCREMENT,
    FullName TEXT,
    DateOfBirth TEXT,
    ScreenName TEXT,
    IsAdult INTEGER,
    PRIMARY KEY (PersonID)
);