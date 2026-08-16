"""
Микро-шаг 123: Переопределение методов родительского класса (Overriding Methods from the Parent Class).
Переопределение метода родителя в классе-наследнике и вызов метода родителя через super().
В ML это позволяет базовому классу определить общий интерфейс, а конкретные модели
переопределяют его своей специфичной логикой.
"""


# Родительский класс: базовая модель машинного обучения
class Model:
    """Базовый класс для любой ML-модели."""

    def __init__(self, name: str, accuracy: float) -> None:
        """Инициализация имени и точности модели."""
        self.name: str = name
        self.accuracy: float = accuracy

    def describe(self) -> None:
        """Общее описание модели."""
        print(f"  Модель: {self.name}")
        print(f"  Точность: {self.accuracy}")


# Класс-наследник: нейросеть (частный случай модели)
class NeuralNetwork(Model):
    """Класс нейросети, наследующий свойства от Model."""

    def __init__(self, name: str, accuracy: float, layers: int) -> None:
        """Инициализация атрибутов родителя и собственных атрибутов."""
        super().__init__(name, accuracy)
        self.layers: int = layers

    def describe(self) -> None:
        """Переопределение метода родителя: расширенное описание нейросети."""
        # Вызов метода родителя через super()
        super().describe()
        # Добавление специфичной информации о нейросети
        print(f"  Количество слоев: {self.layers}")


# Создание экземпляра родительского класса
print("Базовая модель:")
basic_model: Model = Model("Logistic Regression", 0.85)
basic_model.describe()

# Создание экземпляра класса-наследника
print("\nНейросеть (наследник):")
nn_model: NeuralNetwork = NeuralNetwork("Deep CNN", 0.95, 50)
nn_model.describe()