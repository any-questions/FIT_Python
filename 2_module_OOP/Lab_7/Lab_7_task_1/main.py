class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.pages = pages

    def __str__(self):
        return f"{super().__str__()} Количество страниц: {self.pages}"

    def __repr__(self):
        return super().__repr__()


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        if not isinstance(duration, (int, float)):
            raise TypeError("Длительность аудиокниги должна быть типа int или float")
        if duration <= 0:
            raise ValueError("Длительность аудиокниги не может быть меньше нуля")
        self.duration = duration

    def __str__(self):
        return f"{super().__str__()} Продолжительность: {self.duration} часов"

    def __repr__(self):
        return super().__repr__()
