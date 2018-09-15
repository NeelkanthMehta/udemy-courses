"""2018.09.15-Pythhon_Programming-Milestone_Project02"""

from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark book as read
- 'd' to delete a book
- 'q' to quit
<<<<<<< HEAD
Your choice: """

=======
Your choice"""
>>>>>>> d205d2d8a299e851790da6abdd6395f4f10ccf43

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


<<<<<<< HEAD
def prompt_add_book():
=======
def prompt_add_book(): # ask for bookname and author
>>>>>>> d205d2d8a299e851790da6abdd6395f4f10ccf43
    title = input('Enter a new book title: ')
    author = input('Enter the name of the author: ')
    database.add_book(title, author)

<<<<<<< HEAD

def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] == '1' else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")


=======
def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read'] else 'NO'
        print(f"{book['name']} by {book['author']}, read: {read}")

# ask for book name and change it to 'read' in our list
>>>>>>> d205d2d8a299e851790da6abdd6395f4f10ccf43
def prompt_read_book():
    title = input('Enter the title of the book you read: ')
    database.mark_as_read(title)

<<<<<<< HEAD

=======
# ask for book name and remove book from list
>>>>>>> d205d2d8a299e851790da6abdd6395f4f10ccf43
def prompt_delete_books():
    title = input('Enter the name of the book you want to delete: ')
    database.delete_book(title)

<<<<<<< HEAD

menu()
=======
menu()
>>>>>>> d205d2d8a299e851790da6abdd6395f4f10ccf43
