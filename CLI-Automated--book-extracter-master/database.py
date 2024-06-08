
import os
import sqlite3

CREATE_BOOKS_TABLE = "CREATE TABLE IF NOT EXISTS bookDB (id INTEGER PRIMARY KEY, title TEXT, author TEXT, pages INTEGER);"

ADD_BOOK = "INSERT INTO bookDB (title, author, pages) VALUES (?, ?, ?);"

GET_ALL_BOOKS = "SELECT * FROM bookDB;"

GET_BY_TITLE = "SELECT * FROM bookDB WHERE title = ?;"

GET_BY_AUTHOR = "SELECT * FROM bookDB WHERE author = ?;"


def connect():
    return sqlite3.connect("bookDB.db")


def createTable(conn):
    with conn:
        conn.execute(CREATE_BOOKS_TABLE)


def addBook(conn, title, author, pages):
    with conn:
        conn.execute(ADD_BOOK, (title, author, pages))


def getAllBooks(conn):
    with conn:
        return conn.execute(GET_ALL_BOOKS).fetchall()


def getByTitle(conn, title):
    with conn:
        return conn.execute(GET_BY_TITLE, (title, )).fetchall()


def getByAuthor(conn, author):
    with conn:
        return conn.execute(GET_BY_AUTHOR, (author, )).fetchall()
