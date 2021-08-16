DROP TABLE IF EXISTS Temperature;
DROP TABLE IF EXISTS Rain;
DROP TABLE IF EXISTS Humidity;
CREATE TABLE IF NOT EXISTS Temperature (
    year_month TEXT,
    "year" TEXT,
    "month" TEXT,
    temperature REAL,
    PRIMARY KEY (year_month)
);
CREATE TABLE IF NOT EXISTS Rain(
    year_month TEXT,
    "year" TEXT,
    "month" TEXT,
    total REAL,
    max_daily REAL,
    "days" INTEGER,
    PRIMARY KEY (year_month)
);
CREATE TABLE IF NOT EXISTS Humidity(
    year_month TEXT,
    "year" TEXT,
    "month" TEXT,
    "relative" REAL,
    PRIMARY KEY (year_month)
);