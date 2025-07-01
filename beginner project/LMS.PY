class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Available" if not self.is_borrowed else "Borrowed"
        return f"{self.title} by {self.author} ({status})"


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"Sorry, '{book.title}' is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} did not borrow '{book.title}'")

    def __str__(self):
        books = ', '.join(book.title for book in self.borrowed_books) if self.borrowed_books else "No books borrowed"
        return f"User: {self.name}, Borrowed Books: {books}"


if __name__ == "__main__":
    books = [
        Book("The Great Gatsby", "F. Scott Fitzgerald"),
        Book("1984", "George Orwell"),
        Book("To Kill a Mockingbird", "Harper Lee")
    ]

    users = {}

    while True:
        print("\nLibrary Management System")
        print("1. Add User")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display User Details")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter user name: ")
            if name in users:
                print(f"User '{name}' already exists.")
            else:
                users[name] = User(name)
                print(f"User '{name}' added.")

        elif choice == "2":
            print("\nAvailable books:")
            for book in books:
                print(book)

        elif choice == "3":
            user_name = input("Enter user name: ")
            book_title = input("Enter book title: ")
            if user_name in users:
                for book in books:
                    if book.title == book_title:
                        users[user_name].borrow_book(book)
                        break
                else:
                    print("Book not found.")
            else:
                print("User not found.")

        elif choice == "4":
            user_name = input("Enter user name: ")
            book_title = input("Enter book title: ")
            if user_name in users:
                for book in books:
                    if book.title == book_title:
                        users[user_name].return_book(book)
                        break
                else:
                    print("Book not found.")
            else:
                print("User not found.")

        elif choice == "5":
            user_name = input("Enter user name: ")
            if user_name in users:
                print(users[user_name])
            else:
                print("User not found.")

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")