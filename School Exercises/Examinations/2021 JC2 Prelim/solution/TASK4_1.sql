DROP TABLE IF EXISTS "Book";
DROP TABLE IF EXISTS "Printed";
DROP TABLE IF EXISTS "Virtual";
CREATE TABLE IF NOT EXISTS "Book" (
    "BookID" INTEGER,
    "Title" TEXT,
    "Price" INTEGER CHECK("Price" >= 0),
    "Type" TEXT CHECK("Type" = 'physical' OR "Type" = 'virtual'),
    PRIMARY KEY ("BookID")
);
CREATE TABLE IF NOT EXISTS "Printed" (
    "BookID" INTEGER,
    "Weight" INTEGER,
    PRIMARY KEY ("BookID"),
    FOREIGN KEY ("BookID") REFERENCES "Book"("BookID")
);
CREATE TABLE IF NOT EXISTS "Virtual" (
    "BookID" INTEGER,
    "DownloadLink" TEXT,
    PRIMARY KEY ("BookID"),
    FOREIGN KEY ("BookID") REFERENCES "Book"("BookID")
);