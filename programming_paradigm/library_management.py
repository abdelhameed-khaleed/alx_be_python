class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def get_title(self):
        return self.title

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:  # Indentation fixed here
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):  # Remove __books parameter, not needed
        self._books = []  # Use _books consistently

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for b in self._books:  # Use _books, not __books
            if b.get_title() == title and b.is_available():  # Remove quotes around title
                b.check_out()

    def return_book(self, title):
        for b in self._books:  # Use _books, not __books
            if b.get_title() == title and not b.is_available():  # Remove quotes around title
                b.return_book()

    def list_available_books(self):  # Typo fixed in method name
        for b in self._books:  # Use _books, not __books
            if b.is_available():
                print(b.get_title())
