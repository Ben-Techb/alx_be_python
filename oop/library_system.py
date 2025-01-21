# Base Class
class Book:
    def __init__(self, title, author):
        """Initialize a Book instance with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """String representation of a Book."""
        return f"{self.title} by {self.author}"


# Derived Class: EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize an EBook instance."""
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def __str__(self):
        """String representation of an EBook."""
        return f"{super().__str__()} [EBook: {self.file_size}MB]"


# Derived Class: PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize a PrintBook instance."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """String representation of a PrintBook."""
        return f"{super().__str__()} [PrintBook: {self.page_count} pages]"


# Library Class
class Library:
    def __init__(self):
        """Initialize a Library instance."""
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only instances of Book or its subclasses can be added.")

    def list_books(self):
        """List all books in the library."""
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)

