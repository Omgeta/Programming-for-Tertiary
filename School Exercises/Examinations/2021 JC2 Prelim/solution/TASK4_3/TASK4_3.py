# Date: 18/8/2021
# Author: Omgeta
# Description: Task 4.3 Python File
# Version: 1.0

# Dependencies
from flask import Flask
from flask import redirect, render_template, request
from typing import List
import csv

# Vars
app = Flask(__name__)
BOOKS_PATH = "../../bookstore.txt"

# Classes


class Book:
    """Generic Book Class"""

    def __init__(self, title: str, price: int):
        self.title = title
        self.price = price


class PrintedBook(Book):
    """Printed Book Class with Weight"""

    def __init__(self, title: str, price: int, weight: int):
        self.title = title
        self.price = price
        self.weight = weight

    def weight_g(self):
        return f"{self.weight}g"


class VirtualBook(Book):
    """Virtual Book Class with Download Link"""

    def __init__(self, title: str, price: int, download_link: str):
        self.title = title
        self.price = price
        self.download_link = download_link


class Cart:
    """List of Books"""

    def __init__(self, items: List[Book] = []):
        self.items = items

    def total_price(self):
        total_price = 0
        for book in self.items:
            total_price += book.price
        return total_price


# Utilities
def parseBooksFile() -> List[Book]:
    """
    Reads book data and parses it into a list of Book objects
    """
    res = []

    with open(BOOKS_PATH, "r") as f:
        reader = csv.DictReader(
            f, fieldnames=["title", "price", "type", "weight", "download_link"])
        for record in reader:
            # Setting correct types
            price_in_cents = int(float(record["price"]) * 100)

            # Create special book instances and insert into special tables
            if record["type"] == "Physical":
                new_book = PrintedBook(
                    record["title"],  price_in_cents, int(record["weight"]))
            elif record["type"] == "Virtual":
                new_book = VirtualBook(
                    record["title"],  price_in_cents, record["download_link"])

            res.append(new_book)

    return res


all_books = parseBooksFile()


def get_book(bookid: int):
    """Get Book object from the bookid"""
    return all_books[bookid-1]


def get_type(book: Book):
    """Get Book type from the book"""
    if isinstance(book, VirtualBook):
        return "virtual"
    elif isinstance(book, PrintedBook):
        return "physical"


book_cart = Cart()


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html', books=enumerate(all_books, 1), cart=book_cart, get_type=get_type)
    elif request.method == "POST":
        bookid = request.form["bookid"]
        if bookid.isdigit() and 0 < int(bookid) <= len(all_books):
            requested_book = get_book(int(bookid))
            book_cart.items.append(requested_book)
        return redirect("/")


app.run()
