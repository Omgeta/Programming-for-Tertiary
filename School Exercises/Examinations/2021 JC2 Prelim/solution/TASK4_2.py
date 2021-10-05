# Author: Omgeta
# Description: Task 4.2 Python File
# Date: 5/10/2021
# Version: 1.0
from typing import List
import csv
import sqlite3


class Book:
    """ Generic Book Class """

    def __init__(self, title: str, price: int):
        """ Creates book with price in cents and title """
        self.title = title
        self.price = price


class PrintedBook(Book):
    """ Printed Book Class """

    def __init__(self, title: str, price: int, weight: int):
        """ Creates PrintedBook with price in cents, title and weight"""
        super().__init__(title, price)
        self.weight = weight


class VirtualBook(Book):
    """ Virtual Book Class """

    def __init__(self, title: str, price: int, download_link: str):
        """Creates VirtualBook with price in cents, title and download_link """
        super().__init__(title, price)
        self.download_link = download_link


class Cart:
    """ Cart Class for collection of Books """

    def __init__(self, items: List[Book] = []):
        """ Creates a list of Book objects """
        self.items = items

    def total_price(self) -> int:
        """ Sums price of all books in the Cart instance """
        total_price_in_cents = 0
        for book in self.items:
            total_price_in_cents += book.price
        return total_price_in_cents


# Databasing
BOOKSTORE_DATA_FILEPATH = "../bookstore.txt"
BOOKSTORE_DB_FILEPATH = "bookstore.db"


def parse_bookstore_csv(filepath: str) -> List[Book]:
    """
    Parse bookstore CSV file into a list of VirtualBook or PrintedBook objects
    based on the data provided

    Args:
        filepath: Filepath of CSV file to read into
    Returns:
        List of Book objects
    """
    # inialize empty list for appending books later
    res = []

    with open(BOOKSTORE_DATA_FILEPATH, "r") as f:
        reader = csv.reader(f)

        # iterate through all books
        for row in reader:
            # set values to their correct types
            title = str(row[0])
            price_in_cents = int(float(row[1]) * 100)
            book_type = str(row[2])

            # handle different book types
            if book_type == "Physical":
                weight = int(row[3])
                new_book = PrintedBook(title, price_in_cents, weight)
            elif book_type == "Virtual":
                download_link = str(row[4])
                new_book = VirtualBook(title, price_in_cents, download_link)

            # add new book to the list of results
            res.append(new_book)

    return res


def get_conn():
    """ Gets SQLite3 connection to the bookstore DB """
    conn = sqlite3.connect(BOOKSTORE_DB_FILEPATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """ Creates tables in the DB """
    conn = get_conn()
    cur = conn.cursor()

    # get script for building tables
    with open("./TASK4_1.sql", "r", encoding="utf-8") as f:
        script = f.read()
    # f.close() automatically called here

    cur.executescript(script)

    conn.commit()
    conn.close()


def build_db():
    """ Populates tables in the DB """
    conn = get_conn()
    cur = conn.cursor()

    books = parse_bookstore_csv(BOOKSTORE_DATA_FILEPATH)
    for bookid, book in enumerate(books, 1):
        if isinstance(book, PrintedBook):
            book_type = 'physical'
        elif isinstance(book, VirtualBook):
            book_type = 'virtual'

        cur.execute(
            """
            INSERT INTO "Book" (
                "BookID",
                "Title",
                "Price",
                "Type"
            ) VALUES (?, ?, ?, ?);
            """, (bookid, book.title, book.price, book_type)
        )

        if isinstance(book, PrintedBook):
            cur.execute(
                """
                INSERT INTO "Printed" (
                    "BookID",
                    "Weight"
                ) VALUES (?, ?);
                """, (bookid, book.weight)
            )
        elif isinstance(book, VirtualBook):
            cur.execute(
                """
                INSERT INTO "Virtual" (
                    "BookID",
                    "DownloadLink"
                ) VALUES (?, ?);
                """, (bookid, book.download_link)
            )

    conn.commit()
    conn.close()


init_db()
build_db()
