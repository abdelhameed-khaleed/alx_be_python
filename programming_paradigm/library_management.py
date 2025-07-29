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
       if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

class Library:
    def __init__(self, __books):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for b in self.__books:
            if b.get_title() == "title" and b.is_available():
                b.check_out()

    def return_book(self, title):
        for b in self.__books:
            if b.get_title() == "title" and not b.is_available():
                b.return_book()

    def list_avaialble_books(self):
        for b in self.__books:
            if b.is_available():
                print(b.get_title()) 
