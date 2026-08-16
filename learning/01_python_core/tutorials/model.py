"""
Модуль с классом базовой модели машинного обучения.
Это отдельный файл, который можно импортировать в другие скрипты.
"""


class Model:
    """Базовый класс для любой ML-модели."""

    def __init__(self, name: str, accuracy: float) -> None:
        """Инициализация имени и точности модели."""
        self.name: str = name
        self.accuracy: float = accuracy

    def describe(self) -> None:
        """Вывод информации о модели."""
        print(f"  Модель: {self.name}")
        print(f"  Точность: {self.accuracy}")