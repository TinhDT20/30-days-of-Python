# Reading list
list_books =[]
def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the year of publication of the book: ")
    new_book = {
        'title': title,
        'author': author,
        'year': year
    }
    list_books.append(new_book)
    print(f"Your book is added successfully.")
def show_book():
    if len(list_books) == 0:
        print("No books in the list.")
    else:
        for book in list_books:
            print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
def option():
    while True:
        choice = input("What do you want to do? (a: add, s: show, q: quit): ")
        if choice == 'a':
            print("Your choice is to add a book.")
            add_book()
        elif choice == 's':
            print("Your choice is to show all books.")
            show_book()
        elif choice == 'q':
            print("Your choice is to quit the program.")
            break
        else: 
            print("Invalid choice. Please try again.")
option()