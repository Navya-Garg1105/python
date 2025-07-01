class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

class Library:
    def __init__(self):
        self.books = []  # List to store books

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added successfully.")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Book '{title}' removed successfully.")
                return
        print(f"Book '{title}' not found.")

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"Book found: {book}")
                return
        print(f"Book '{title}' not found.")

    def display_books(self):
        if self.books:
            print("\nBooks available in the library:")
            for book in self.books:
                print(f"- {book}")
        else:
            print("The library is empty.")

# Example usage:
library = Library()

while True:
    print("\n1. Add Book\n2. Remove Book\n3. Search Book\n4. Display Books\n5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        library.add_book(Book(title, author))
    elif choice == 2:
        title = input("Enter book title to remove: ")
        library.remove_book(title)
    elif choice == 3:
        title = input("Enter book title to search: ")
        library.search_book(title)
    elif choice == 4:
        library.display_books()
    elif choice == 5:
        print("Thank you for using the library system!")
        break
    else:
        print("Invalid choice. Please try again.")
