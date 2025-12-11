class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self):
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise TypeError("Only Book instances can be added.")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(f"{book.title} by {book.author}")
        if not available_books:
            print("No books available.")
