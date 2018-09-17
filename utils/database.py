from typing import List, Dict, Union

from utils.database_connection import DatabaseConnection
# Concerned with storing and retreiving books from a list

Book = Dict[str, Union[str, int]]


def create_book_table():
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(title text primary key, author text, read integer)')


def get_all_books() -> List[Book]:
    # load the list of books
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()

        cursor.execute('SELECT title, author, read FROM books')
        books = [{'title': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    return books


def add_book(title: str, author: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (title, author))


def mark_as_read(title: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('UPDATE books SET read=1 WHERE title=?', (title,))


def delete_book(title: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        cursor.execute('DELETE FROM books WHERE title=?', (title,))
