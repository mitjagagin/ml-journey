"""Тесты для функции format_name из шага 152."""
import unittest

# Импортируем функцию из папки tutorials
from tutorials.step_152_testing_function import format_name


class NamesTestCase(unittest.TestCase):
    """Тесты для функции format_name."""

    def test_first_last_name(self) -> None:
        """Тестирует форматирование имени и фамилии (например, 'janis joplin')."""
        formatted_name: str = format_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


if __name__ == '__main__':
    unittest.main()