class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Library:
    def __init__(self):
        self.books = []
    
    # Implement this
    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)
    
    # Implement this
    def search_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return True
        return False

        
# Test Input
lib = Library()
lib.add_book("1984", "George Orwell")
print(lib.search_by_title("1985")) 