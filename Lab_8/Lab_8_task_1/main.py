from abc import ABC, abstractmethod

class Microcontroller(ABC):
    """
    Базовый класс - микроконтроллеры.
    """
    def __init__(self, model: str, architecture: str, pins: int):
        """
        Ининциализация объекта "микроконтроллер"

            :param model (str): Модель микроконтроллера
            :param architecture (str): Архитектура микроконтроллера
            :param pins (int): Количество GPIO пинов микроконтроллера

        """
        if not isinstance(model, str):
            raise TypeError("Модель микроконтроллера должна быть строкой")
        self.model = model
        if not isinstance(model, str):
            raise TypeError("Название архитектуры микроконтроллера должно быть строкой")
        self.architecture = architecture
        if not isinstance(pins, int):
            raise TypeError("Количетство пинов должено быть целым числом")
        if pins < 0:
            raise ValueError("Количество пинов не может быть меньше 0")
        self.pins = pins

    def __str__(self):
        """
        Возвращает информауию о микроконтроллере в виде строки
        """
        return f"{self.model} - Architecture: {self.architecture}, Pins: {self.pins}"

    def __repr__(self):
        """
        Возвращает детальтную информауию о микроконтроллере в виде строки
        """
        return f"Microcontroller(model={self.model}, architecture={self.architecture}, pins={self.pins})"

    @abstractmethod
    def program(self, code: str):
        """
        Абстрактный метод программирования микроконтроллера


            :param code (str): Код, который необходимо запрограммировать в микроконтроллер
        """
        pass

class AVR(Microcontroller):
    """
    Дочерний класс, представляющий микроконтроллер серии AVR
    """
    def __init__(self, model: str, pins: int, frequency: int):
        """
        Ининциализация AVR микроконтроллера

            :param model (str): Модель микроконтроллера
            :param pins (int): Количество GPIO пинов микроконтроллера
            :param frequency (int): Рабрчая частота микроконтроллера, Гц
        """
        super().__init__(model, "AVR", pins)
        if not isinstance(frequency, int):
            raise TypeError("Частота тактирования должна быть целым числом")
        if frequency < 0:
            raise ValueError("Частота тактирования не может быть меньше 0")
        self.frequency = frequency

    def __str__(self):
        """
        Возвращает информауию о микроконтроллере в виде строки
        """
        return super().__str__() + f", Frequency: {self.frequency} MHz"

    def __repr__(self):
        """
        Возвращает детальтную информауию о микроконтроллере в виде строки
        """
        return f"AVR(model={self.model}, pins={self.pins}, frequency={self.frequency})"

    def program(self, code: str):
        """
        Программирование микроконтроллера AVR с помощью предоставленного кода

            :param code (str): Код, который необходимо запрограммировать в микроконтроллер
        Этот метод перегружен для конкретной реализации программирования AVR микроконтроллера

        Возвращает:
            :bool: 1 (Истина), если програмирование прошло успешно, и 0 (Ложь), если не удалось запрограмировать контроллер
        """
        # Услованя реализация программирования выделенного микроконтроллера (AVR).
        pass

    def flash_led(self, pin: int):
        """
        Мигание светодиодом, подключенным к определенному выводу микроконтроллера AVR (пр. - 13 пин).

            :param pin (int): Пин, к которому подключен светодиод
            Метод flash_led добавлен для расширения функционала дочернего класса

         Возвращает:
            :bool: 1 (Истина), если мигание прошло успешно, и 0 (Ложь), если не удалось помигать светодиодом
        """
        # Условная реализация мигания светоджиодом на выбраном пине
        pass

if __name__ == "__main__":
    MC = AVR("ATmega 328p", 23, 16000000)
    MC.flash_led(13)
    print(MC)
    pass