"""
Микро-шаг 111: Метод __init__() (The __init__() Method).
Детальный разбор конструктора класса и создания атрибутов.
В ML метод __init__ используется для инициализации гиперпараметров
(настроек модели) и подготовки объекта к обучению.
"""


class MLModel:
    """Простая модель машинного обучения."""

    def __init__(self, algorithm: str, learning_rate: float) -> None:
        """Инициализирует атрибуты модели."""
        self.algorithm: str = algorithm
        self.learning_rate: float = learning_rate

    def describe(self) -> None:
        """Выводит описание модели и её гиперпараметры."""
        print(f"Алгоритм: {self.algorithm}, Learning rate: {self.learning_rate}")


# Создаем первый экземпляр (модель А)
model_a: MLModel = MLModel("LinearRegression", 0.01)

# Создаем второй экземпляр (модель B) с другими настройками
model_b: MLModel = MLModel("LogisticRegression", 0.1)

print("Экземпляр А:")
model_a.describe()

print("\nЭкземпляр B:")
model_b.describe()

# Проверяем, что атрибуты принадлежат конкретным объектам
print("\nПрямое обращение к атрибутам:")
print(f"  model_a.algorithm = {model_a.algorithm}")
print(f"  model_b.learning_rate = {model_b.learning_rate}")