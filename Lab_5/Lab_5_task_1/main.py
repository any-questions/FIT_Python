
class Plant:
    def __init__(self, species: str, height: float):
        """
        Создание и подготовка к работе объекта "Растение"

        :species: Вид растения
        :height: Высота растения

        Примеры:
        >>> Beryoza = Plant("Beryoza", 9.11)  # инициализация экземпляра класса
        """

        if not isinstance(species, (str)):
            raise TypeError("Название растения должно быть типа str")
        self.species = species

        if not isinstance(height, (int, float)):
            raise TypeError("Высота растения должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота растения должна положительным числом")
        self.height = height

    def grow(self, growth_rate: float) -> None:
        """
        Функция, заставляющая растение расти с заданной скоростью.

        Примеры:
        >>> Beryoza = Plant("Beryoza", 9.11)
        >>> Beryoza.grow(1.1)
        """
        if not isinstance(growth_rate, (int, float)):
            raise TypeError("Скорость роста должна быть типа int или float")
        if growth_rate < 0:
            raise ValueError("Скорость роста должна положительным числом")
        ...


    def get_info(self) -> str:
        """
        Функция, возвращающая вид растения

        :return: Возвращает название вида растения

        Примеры:
        >>> Beryoza = Plant("Beryoza", 9.11)
        >>> Beryoza.get_info()
        """
        ...


class Book:
    def __init__(self, title: str, author: str, num_pages: int):
        """
        Инициализация объекта "Книга".

        :title: Название книги
        :author: Автор книги
        :num_pages: Количество страниц в книге

        Примеры:
        >>> book = Book("Мастер и Маргарита", "Михаил Булгаков", 400)
        """

        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Автор книги должен быть строкой")
        self.author = author

        if not isinstance(num_pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if num_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.num_pages = num_pages

    def read(self, pages: int) -> None:
        """
        Функция, представляющая чтение книги.

        :pages: Количество страниц для чтения

        Примеры:
        >>> book = Book("Мастер и Маргарита", "Михаил Булгаков", 400)
        >>> book.read(10)
        """
        ...

    def get_summary(self) -> str:
        """
        Функция, возвращающая краткое содержание книги.

        :return: Строка с кратким содержанием книги

        Примеры:
        >>> book = Book("Мастер и Маргарита", "Михаил Булгаков", 400)
        >>> book.get_summary()
        """
        ...


class Vehicle:
    def __init__(self, brand: str, model: str, year: int,motor_capacity: float, horse_power:int, fuel_capacity:float):
        """
        Инициализация объекта "Автомобиль".

        :brand: Марка автомобиля
        :model: Модель автомобиля
        :year: Год выпуска автомобиля
        :fuel_capacity: Объем топливного бака в литрах
        :horse_power: Количество лошадиных сил в автомобиле
        :fuel_capacity: Объем топливного бака в литрах

        Примеры:
        >>> car = Vehicle("Nissan", "Skyline R34", 2002, 2.5, 280, 65)
        """

        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть строкой")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Модель автомобиля должна быть строкой")
        self.model = model

        if not isinstance(year, int):
            raise TypeError("Год выпуска должен быть целым числом")
        if year < 1886 or year > 2024:  # Первый год автомобиля и максимально возможный год в будущем
            raise ValueError("Год выпуска автомобиля некорректен")
        self.year = year

        if not isinstance(motor_capacity, (int, float)):
            raise TypeError("Объем мотора должен быть числом")
        if motor_capacity <= 0:
            raise ValueError("Объем мотора бака должен быть положительным числом")
        self.fuel_capacity = motor_capacity

        if not isinstance(horse_power, (int)):
            raise TypeError("Количество лошадиных сил должно быть целым числом")
        if horse_power <= 0:
            raise ValueError("Количество лошадиных сил должно быть положительным числом")
        self.horse_power = horse_power

        if not isinstance(fuel_capacity, (int, float)):
            raise TypeError("Объем топливного бака должен быть числом")
        if fuel_capacity <= 0:
            raise ValueError("Объем топливного бака должен быть положительным числом")
        self.fuel_capacity = fuel_capacity

    def start_engine(self) -> None:
        """
        Функция, представляющая запуск двигателя автомобиля.

        Примеры:
        >>> car = Vehicle("Nissan", "Skyline R34", 2002, 2.5, 280, 65)
        >>> car.start_engine()
        """
        ...

    def refuel(self, liters: float) -> None:
        """
        Функция, представляющая заправку топлива в автомобиль.

        :liters: Количество литров топлива для заправки

        Примеры:
        >>> car = Vehicle("Nissan", "Skyline R34", 2002, 2.5, 280, 65)
        >>> car.refuel(30)
        """
        if not isinstance(liters, (int, float)):
            raise TypeError("Количество заправляемого топлива должно быть int или float")
        if liters < 0:
            raise ValueError("Количество заправляемого топлива не может быть меньше нуля")
        ...
    def engine_forcing(self, now_horse_power: int) -> None:
        """
        Функция, представляющая заправку топлива в автомобиль.

        :liters: Количество литров топлива для заправки

        Примеры:
        >>> car = Vehicle("Nissan", "Skyline R34", 2002, 2.5, 280, 65)
        >>> car.engine_forcing(30)
        """
        if not isinstance(now_horse_power, (int)):
            raise TypeError("Количество лошадиных сил должно быть целым числом")
        if now_horse_power < 0:
            raise ValueError("Количество лошадиных сил должно положительным числом")
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()  # тестирование примеров, которые находятся в документации