
from book_shelf import BookShelf
from book import Book


def main():
    book_shelf = BookShelf()
    book_shelf.append_book(Book('21天精通Java'))
    book_shelf.append_book(Book('21天精通C++'))
    book_shelf.append_book(Book('21天精通PHP'))
    book_shelf.append_book(Book('21天精通Python'))

    for book in book_shelf:
        print(book.get_name())


if __name__ == '__main__':
    main()


