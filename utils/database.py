# Concerned with storing and retreiving books from a list

books = []

def add_book(title, author):
    books.append({'name': title, 'author': author,'read': False})

def get_all_books():
    return books

def mark_as_read(title):
    for book in books:
        if book['name'] == title:
            book['read'] == True
    # {book['read']: True for book in books if book['name'] == title}

def delete_book(title):
    global books
    books = [book for book in books if book['name'] != title]