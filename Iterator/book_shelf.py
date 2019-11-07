
class BookShelf:

    def __init__(self):
        self._books = []
        self._last = 0

    def get_book_at(self, index):
        return self._books[index]

    def append_book(self, book):
        self._books.append(book)
        self._last += 1

    def get_length(self):
        return self._last

    def __iter__(self):
        for book in self._books:
            yield book
