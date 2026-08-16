"""
Модуль с классами предобработчиков (подготовителей данных для модели).
Содержит три класса для разных стратегий предобработки признаков (колонок данных).
"""


class StandardScaler:
    """Предобработчик: стандартизация (приведение к среднему 0 и дисперсии 1)."""

    def __init__(self) -> None:
        """Инициализация предобработчика."""
        self.name: str = "StandardScaler"
        self.is_fitted: bool = False

    def fit(self) -> None:
        """Обучение предобработчика на данных."""
        self.is_fitted = True
        print(f"  {self.name} обучен")

    def describe(self) -> None:
        """Вывод информации о предобработчике."""
        status: str = "обучен" if self.is_fitted else "не обучен"
        print(f"  Предобработчик: {self.name} ({status})")


class MinMaxScaler:
    """Предобработчик: масштабирование к диапазону [0, 1]."""

    def __init__(self) -> None:
        """Инициализация предобработчика."""
        self.name: str = "MinMaxScaler"
        self.is_fitted: bool = False

    def fit(self) -> None:
        """Обучение предобработчика на данных."""
        self.is_fitted = True
        print(f"  {self.name} обучен")

    def describe(self) -> None:
        """Вывод информации о предобработчике."""
        status: str = "обучен" if self.is_fitted else "не обучен"
        print(f"  Предобработчик: {self.name} ({status})")


class LabelEncoder:
    """Предобработчик: кодирование категорий (превращение текста в числа)."""

    def __init__(self) -> None:
        """Инициализация предобработчика."""
        self.name: str = "LabelEncoder"
        self.is_fitted: bool = False

    def fit(self) -> None:
        """Обучение предобработчика на данных."""
        self.is_fitted = True
        print(f"  {self.name} обучен")

    def describe(self) -> None:
        """Вывод информации о предобработчике."""
        status: str = "обучен" if self.is_fitted else "не обучен"
        print(f"  Предобработчик: {self.name} ({status})")