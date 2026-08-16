"""
Микро-шаг 121: Метод __init__() для класса-наследника (The __init__() Method for a Child Class).
Создание класса-наследника и вызов конструктора родительского класса через super().
В ML это используется для построения иерархий моделей, где базовый класс задает общие
свойства, а наследник добавляет специфичные параметры (например, слои нейросети).
"""


# Родительский класс: базовая модель машинного обучения
class Model:
    """Базовый класс для любой ML-модели."""

    def __init__(self, name: str, accuracy: float) -> None:
        """Инициализация имени и точности модели."""
        self.name: str = name
        self.accuracy: float = accuracy


# Класс-наследник: нейросеть (частный случай модели)
class NeuralNetwork(Model):
    """Класс нейросети, наследующий свойства от Model."""

    def __init__(self, name: str, accuracy: float, layers: int) -> None:
        """Инициализация атрибутов родителя и собственных атрибутов."""
        # Вызов метода __init__() родительского класса Model
        super().__init__(name, accuracy)
        # Добавление специфичного атрибута для нейросети
        self.layers: int = layers


# Создание экземпляра родительского класса
print("Базовая модель:")
basic_model: Model = Model("Logistic Regression", 0.85)
print(f"  Имя: {basic_model.name}")
print(f"  Точность: {basic_model.accuracy}")

# Создание экземпляра класса-наследника
print("\nНейросеть (наследник):")
nn_model: NeuralNetwork = NeuralNetwork("Deep CNN", 0.95, 50)
print(f"  Имя: {nn_model.name}")
print(f"  Точность: {nn_model.accuracy}")
print(f"  Количество слоев: {nn_model.layers}")