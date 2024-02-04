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

        :return: Строка с экземпляром класса.
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


# TODO написать класс Book


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
