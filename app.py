"""2018.09.15-Pythhon_Programming-Milestone_Project02"""

from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark book as read
- 'd' to delete a book
- 'q' to quit
Your choice"""

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_books()
        else:
            print('Unknown command, please try again.')
        user_input = input(USER_CHOICE)


def prompt_add_book(): # ask for bookname and author
    title = input('Enter a new book title: ')
    author = input('Enter the name of the author: ')
    database.add_book(title, author)

def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")

# ask for book name and change it to 'read' in our list
def prompt_read_book():
    title = input('Enter the title of the book you read: ')
    database.mark_as_read(title)

# ask for book name and remove book from list
def prompt_delete_books():
    title = input('Enter the name of the book you want to delete: ')
    database.delete_book(title)

menu()