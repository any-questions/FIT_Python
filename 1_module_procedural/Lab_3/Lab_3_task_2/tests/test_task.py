import inspect
import unittest

try:
    from task import find_common_participants
except ImportError:
    raise AssertionError(
        'Проверьте, что объявлена функция `find_common_participants`'
    )


class TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        sign = inspect.signature(find_common_participants)
        assert len(sign.parameters) == 3, (
            'Убедитесь, что при объявлении функции `find_common_participants` '
            'указано три аргумента.'
        )

        first_arg, second_arg, third_arg = inspect.signature(find_common_participants).parameters.values()
        assert first_arg.default == inspect.Parameter.empty, (
            f'Убедитесь, что первый аргумент {first_arg.name} функции '
            f'`find_common_participants` является позиционным аргументом.'
        )

        assert second_arg.default == inspect.Parameter.empty, (
            f'Убедитесь, что первый аргумент {second_arg.name} функции '
            f'`find_common_participants` является позиционным аргументом.'
        )

        expected_default_value = ','
        assert third_arg.default == expected_default_value, (
            f'Убедитесь, что третий аргумент {third_arg.name} функции '
            f'`find_common_participants` является аргументом по умолчанию.'
        )

    def test_find_common_participants(self):
        participants1 = "Иванов,Петров,Сидоров"
        participants2 = "Петров,Сидоров,Смирнов"

        expected_result = ['Петров', 'Сидоров']
        actual_result = find_common_participants(participants1, participants2)

        assert isinstance(actual_result, list), (
            'Убедитесь, что функция `find_common_participants` возвращает список.'
        )

        assert actual_result == expected_result, (
            'Убедитесь, что верно реализована логика нахождения '
            'общих участников в функции `find_common_participants`'
        )

    def test_find_common_participants_other_sep(self):
        participants1 = "Иванов;Петров;Сидоров"
        participants2 = "Петров;Сидоров;Смирнов"
        sep = ";"

        expected_result = ['Петров', 'Сидоров']
        actual_result = find_common_participants(participants1, participants2, sep)

        assert actual_result == expected_result, (
            'Убедитесь, что функция `find_common_participants` '
            'умеет разделять строку с участниками отличным от запятой.'
        )
