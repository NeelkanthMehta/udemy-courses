<<<<<<< HEAD
# Concerned with storing and retrieving books from a list

books_file = 'books.txt'


def add_book(title, author):
    with open('books.txt', 'a') as file:
        file.write(f"{title}, {author}, 0 \n")
    # books.append({'name': title, 'author': author, 'read': False})


def get_all_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]
    return [{'name': line[0], 'author': line[1], 'read': line[2]} for line in lines]
    # return [line.rstrip('\n').split(',') for line in open(books_file, 'r')]


def mark_as_read(title):
    books = get_all_books()
    for book in books:
        if book['name'] == title:
            book['read'] = '1'
    _save_all_books(books)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']}, {book['author']}, {book['read']}\n")


def delete_book(title):
    books = get_all_books()
    books = [book for book in books if book['name'] != title]
    _save_all_books(books)
    # global books
    # books = [book for book in books if book['name'] != title]
=======
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
>>>>>>> d205d2d8a299e851790da6abdd6395f4f10ccf43
