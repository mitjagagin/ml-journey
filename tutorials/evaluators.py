"""
Модуль с классами оценщиков моделей.
Содержит классы для разных способов оценки качества моделей.
"""


class CrossValidator:
    """Кросс-валидатор (оценка модели на нескольких подвыборках данных)."""

    def __init__(self, num_folds: int) -> None:
        """Инициализация количества подвыборок (folds)."""
        self.num_folds: int = num_folds
        self.is_fitted: bool = False

    def evaluate(self, model_name: str) -> None:
        """Запуск кросс-валидации."""
        self.is_fitted = True
        print(f"  Кросс-валидация запущена: {self.num_folds} подвыборок для модели {model_name}")

    def describe(self) -> None:
        """Вывод информации о кросс-валидаторе."""
        status: str = "использован" if self.is_fitted else "не использован"
        print(f"  Кросс-валидатор: {self.num_folds} подвыборок ({status})")


class HoldoutEvaluator:
    """Оценщик на отложенной выборке (отдельной части данных для финальной проверки)."""

    def __init__(self, test_size: float) -> None:
        """Инициализация доли тестовых данных."""
        self.test_size: float = test_size
        self.is_fitted: bool = False

    def evaluate(self, model_name: str) -> None:
        """Запуск оценки на отложенной выборке."""
        self.is_fitted = True
        print(f"  Оценка на отложенной выборке: {self.test_size} от данных для модели {model_name}")

    def describe(self) -> None:
        """Вывод информации об оценщике."""
        status: str = "использован" if self.is_fitted else "не использован"
        print(f"  Holdout-оценщик: тестовая доля {self.test_size} ({status})")