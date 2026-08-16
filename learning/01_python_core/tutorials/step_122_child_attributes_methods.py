"""
Микро-шаг 122: Определение атрибутов и методов для класса-наследника (Defining Attributes and Methods for the Child Class).
Добавление уникальных атрибутов и методов, которые отличают наследника от родителя.
В ML это позволяет добавлять специфичные параметры (например, скорость обучения)
и методы (например, настройку архитектуры) только для конкретных типов моделей.
"""


# Родительский класс: базовая модель машинного обучения
class Model:
    """Базовый класс для любой ML-модели."""

    def __init__(self, name: str, accuracy: float) -> None:
        """Инициализация имени и точности модели."""
        self.name: str = name
        self.accuracy: float = accuracy

    def display_name(self) -> None:
        """Вывод имени модели."""
        print(f"Модель: {self.name}")


# Класс-наследник: нейросеть (частный случай модели)
class NeuralNetwork(Model):
    """Класс нейросети, наследующий свойства от Model."""

    def __init__(self, name: str, accuracy: float, layers: int) -> None:
        """Инициализация атрибутов родителя и собственных атрибутов."""
        super().__init__(name, accuracy)
        self.layers: int = layers
        # Добавление атрибута со значением по умолчанию, специфичного для нейросети
        self.learning_rate: float = 0.01

    def describe_layers(self) -> None:
        """Вывод информации о количестве слоев (метод только для наследника)."""
        print(f"  Количество слоев: {self.layers}")

    def describe_learning_rate(self) -> None:
        """Вывод информации о скорости обучения (метод только для наследника)."""
        print(f"  Скорость обучения: {self.learning_rate}")


# Создание экземпляра класса-наследника
print("Нейросеть (наследник):")
nn_model: NeuralNetwork = NeuralNetwork("Deep CNN", 0.95, 50)

# Вызов метода, унаследованного от родителя
nn_model.display_name()

# Вызов новых методов, которые есть только у NeuralNetwork
print("Специфичные атрибуты:")
nn_model.describe_layers()
nn_model.describe_learning_rate()