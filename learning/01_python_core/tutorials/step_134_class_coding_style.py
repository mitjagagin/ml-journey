"""
Микро-шаг 134: Стиль кодирования классов (Class Coding Style / PEP 8).
Стандартные правила оформления классов для профессионального кода.
В ML-инженерии соблюдение PEP 8 обязательно: это обеспечивает читаемость
кода в команде и облегчает поддержку ML-пайплайнов (последовательностей обработки данных).
"""


# ПРАВИЛО 1: Имена классов — CamelCase (с заглавной буквы каждого слова)
# ПРАВИЛО 2: Имена экземпляров и методов — snake_case (строчные с подчёркиваниями)


class RandomForestClassifier:
    """Классификатор на основе случайного леса.

    Случайный лес — это ансамбль (объединение) решающих деревьев,
    который даёт более точные предсказания, чем одно дерево.

    Attributes:
        n_estimators: Количество деревьев в лесе.
        max_depth: Максимальная глубина каждого дерева.
        is_fitted: Флаг, показывающий, обучена ли модель.
    """

    def __init__(self, n_estimators: int, max_depth: int) -> None:
        """Инициализация параметров случайного леса.

        Args:
            n_estimators: Количество деревьев в лесе.
            max_depth: Максимальная глубина каждого дерева.
        """
        self.n_estimators: int = n_estimators
        self.max_depth: int = max_depth
        self.is_fitted: bool = False

    def fit(self, x_train: list[float], y_train: list[int]) -> None:
        """Обучение модели на тренировочных данных.

        Args:
            x_train: Признаки (features) тренировочных данных.
            y_train: Целевые значения тренировочных данных.
        """
        self.is_fitted = True
        print(f"  Модель обучена: {self.n_estimators} деревьев, глубина {self.max_depth}")

    def predict(self, x_test: list[float]) -> list[int]:
        """Предсказание на новых данных.

        Args:
            x_test: Признаки тестовых данных.

        Returns:
            Список предсказанных классов.
        """
        if not self.is_fitted:
            print("  Ошибка: модель не обучена")
            return []
        print(f"  Предсказание для {len(x_test)} примеров")
        return [1] * len(x_test)

    def describe(self) -> None:
        """Вывод информации о модели."""
        status: str = "обучена" if self.is_fitted else "не обучена"
        print(f"  Модель: RandomForestClassifier ({status})")
        print(f"  Деревьев: {self.n_estimators}, максимальная глубина: {self.max_depth}")


# ПРАВИЛО 3: Пустая строка между методами (одна строка)
# ПРАВИЛО 4: Две пустые строки между классами


class LogisticRegressionModel:
    """Логистическая регрессия для бинарной классификации."""

    def __init__(self) -> None:
        """Инициализация модели."""
        self.is_fitted: bool = False

    def fit(self) -> None:
        """Обучение модели."""
        self.is_fitted = True
        print("  LogisticRegression обучена")


# Использование классов с правильным оформлением
print("Пример классов в стиле PEP 8:")
rf_model: RandomForestClassifier = RandomForestClassifier(n_estimators=100, max_depth=10)
rf_model.describe()

print("\nОбучение и предсказание:")
rf_model.fit(x_train=[1.0, 2.0, 3.0], y_train=[0, 1, 0])
predictions: list[int] = rf_model.predict(x_test=[1.5, 2.5])

print("\nВторая модель:")
lr_model: LogisticRegressionModel = LogisticRegressionModel()
lr_model.fit()