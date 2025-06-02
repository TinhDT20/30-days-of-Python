menu_option = """ please select an option:

- 'a' to add a book
- 'l' to list all books
- 'd' to delete a book
- 'r' to mark a book as read
- 's' to search for a book
- 'q' to quit

What would you like to do? """

def add_book(): #add
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the year of publication of the book: ")

    with open("books.csv", "a") as f:
        f.write(f"{title},{author},{year}\n")

def delete_book(books, book_to_delete): ## delete
    books.remove(book_to_delete)

def list_books():
    books = []
    with open("books.csv", "r") as f:
        for book in f:
            title, author, year, status = book.strip().split(",")
            books.append({
                "title": title,
                "author": author,
                "year": year,
                "status": status
            })
            
    return books

def search_book():
    reading_list = list_books()
    search_term = input("Enter the title or author of the book to search: ").strip().lower()
    matching_books = []

    search_term = input("Enter the title of the book to search: ").strip().lower()
    for book in reading_list:
        if book['title'].lower() == search_term:
            matching_books.append(book)

    return matching_books
def mark_as_read():
def show_list_books():
    books = list_books()
    for book in books:
        print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Status: {book['status']}")

def option():
    while True:
        selected_option = input(menu_option).strip().lower()
        if selected_option == 'a':
            print("Your choice is to add a book.")
            add_book()
        elif selected_option == 'd':
            print("Your choice is to delete a book.")
            delete_book()
        elif selected_option == 'r':
            print("Your choice is to mark a book as read.")
            mark_as_read()
        elif selected_option == 's':
            print("Your choice is to search for a book.")
            search_book()
        elif selected_option == 'l':
            print("Your choice is to list all books.")
            show_list_books()
        elif selected_option == 'q':
            print("Your choice is to quit the program.")
            break
        else: 
            print("Invalid choice. Please try again.")

option()