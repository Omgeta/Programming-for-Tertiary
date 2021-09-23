DROP TABLE IF EXISTS People;
CREATE TABLE IF NOT EXISTS People(
    PersonID INTEGER PRIMARY KEY AUTOINCREMENT,
    FullName TEXT,
    DateOfBirth TEXT,
    ScreenName TEXT,
    IsAdult INTEGER
);