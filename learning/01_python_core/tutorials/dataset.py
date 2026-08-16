"""
Модуль с классами для работы с данными.
Содержит два связанных класса: Dataset (датасет) и Preprocessor (предобработчик).
"""


class Dataset:
    """Датасет (набор данных) для обучения модели."""

    def __init__(self, name: str, num_rows: int) -> None:
        """Инициализация имени и количества строк."""
        self.name: str = name
        self.num_rows: int = num_rows

    def describe(self) -> None:
        """Вывод информации о датасете."""
        print(f"  Датасет: {self.name}")
        print(f"  Строк: {self.num_rows}")


class Preprocessor:
    """Предобработчик (подготавливает данные для модели)."""

    def __init__(self, strategy: str) -> None:
        """Инициализация стратегии предобработки."""
        self.strategy: str = strategy
        self.is_fitted: bool = False

    def fit(self) -> None:
        """Обучение предобработчика на данных."""
        self.is_fitted = True
        print(f"  Предобработчик обучен (стратегия: {self.strategy})")

    def describe(self) -> None:
        """Вывод информации о предобработчике."""
        status: str = "обучен" if self.is_fitted else "не обучен"
        print(f"  Предобработчик: {self.strategy} ({status})")