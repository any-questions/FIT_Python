BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int):
        """
        Инициализация объекта "Книга".

        :param id_: Идентификатор книги.
        :param name: Название книги.
        :param pages: Количество страниц в книге.
        """
        self.id = id_
        self.name = name
        if not isinstance(pages, (int)):
            raise TypeError("Количество страниц сил должно быть целым числом")
        if pages < 0:
            raise ValueError("Количество страниц сил должно положительным числом")
        self.pages = pages

    def __str__(self) -> str:
        """
        Метод возвращает строку формата, где "название_книги" берется с помощью атрибута name.

        :return: Строка формата "Книга "название_книги""
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Метод возвращает строку, по которой можно инициализировать экземпляр.

        :return: Строка с представлением экземпляра класса.
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


# TODO написать класс Book


class Library:
    def __init__(self, books=None):
        """
        Инициализация объекта "Библиотека".

        :param books: Список книг (по умолчанию None).
        """
        self.books = books or []

    def get_next_book_id(self) -> int:
        """
        Метод возвращает идентификатор для добавления новой книги в библиотеку.

        :return: Идентификатор для новой книги.
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Метод возвращает индекс книги в списке по идентификатору.

        :param book_id: Идентификатор книги.
        :return: Индекс книги в списке.
        :raises ValueError: Если книги с заданным id не существует.
        """
        for index, book in enumerate(self.books): #твродде эта функция?
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


# TODO написать класс Library


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
