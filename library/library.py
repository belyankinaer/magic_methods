from library.book import Book


class Library:
    def __init__(self, books: list = []):
        self.__books = books

    def __setitem__(self, book: Book):
        if not book:
            print("Информации о книге нет, добавить не получится")
            return

        if book in self.__books:
            print("Книга уже есть в библиотеке")
            return

        self.__books.append(book)

    def __getitem__(self, book_name: str):
        for book in self.__books:
            if book.get_name() == book_name:
                return book

    def __len__(self):
        if self.__books:
            return len(self.__books)
