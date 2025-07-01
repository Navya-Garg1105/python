class Library:
    def __init__(self, name):
        self.name = name
        self.books = []  # List to store books

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print(f"Books available in {self.name}:")
            for book in self.books:
                print(f"- {book.title} by {book.author}")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False

class LibraryManagementSystem(Library):
    def issue_book(self, book_title, user):
        for book in self.books:
            if book.title == book_title:
                if not book.is_issued:
                    book.is_issued = True
                    print(f"Book '{book.title}' has been issued to {user}.")
                    return
                else:
                    print(f"Sorry, the book '{book.title}' is already issued.")
                    return
        print(f"Book '{book_title}' not found in the library.")

    def return_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                if book.is_issued:
                    book.is_issued = False
                    print(f"Book '{book.title}' has been returned.")
                    return
                else:
                    print(f"The book '{book.title}' was not issued.")
                    return
        print(f"Book '{book_title}' not found in the library.")

# Example Usage
if __name__ == "__main__":
    library_name = "Welcome to GLAU library"
    library = LibraryManagementSystem(library_name)

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            book = Book(title, author)
            library.add_book(book)

        elif choice == "2":
            library.display_books()

        elif choice == "3":
            book_title = input("Enter the title of the book to issue: ")
            user = input("Enter the name of the user: ")
            library.issue_book(book_title, user)

        elif choice == "4":
            book_title = input("Enter the title of the book to return: ")
            library.return_book(book_title)

        elif choice == "5":
            print("Exiting Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
