# Concerned with storing and retreiving books from a list

books_file = 'books.txt'


def create_book_table():
    with open(books_file, "w+") as file:
        pass


def get_all_books():
    # load the list of books
    with open(books_file, "r+") as file:
        lines = [line.strip().split(',') for line in file.readlines()]
    return [{'title': line[0], 'author': line[1], 'read': line[2]} for line in lines]


def add_book(title, author):
    with open(books_file, 'a+') as file:
        file.writelines(f"{title}, {author}, 0\n")
    # books.append({'name': title, 'author': author,'read': False})


def _save_all_books(books):
    with open(books_file, 'w+') as file:
        for book in books:
            file.write(f"{book['title']}, {book['author']}, {book['read']}\n")


def mark_as_read(title):
    books = get_all_books()
    for book in books:
        if book['title'] == title:
            book['read'] = '1'
    _save_all_books(books)
    # {book['read']: True for book in books if book['name'] == title}


def delete_book(title):
    books = get_all_books()
    books = [book for book in books if book['title'] != title]
    _save_all_books(books)
