"""
Микро-шаг 124: Экземпляры как атрибуты (Instances as Attributes).
Использование экземпляра одного класса как атрибута другого класса.
В ML это применяется для композиции: модель содержит объект-оптимизатор
с настройками обучения, объект-датасет и другие компоненты.
"""


# Класс для хранения настроек оптимизатора
class Optimizer:
    """Настройки оптимизатора (алгоритма обновления весов модели)."""

    def __init__(self, learning_rate: float, name: str) -> None:
        """Инициализация скорости обучения и имени оптимизатора."""
        self.learning_rate: float = learning_rate
        self.name: str = name

    def describe(self) -> None:
        """Вывод информации об оптимизаторе."""
        print(f"  Оптимизатор: {self.name}")
        print(f"  Скорость обучения: {self.learning_rate}")


# Родительский класс: базовая модель
class Model:
    """Базовый класс для любой ML-модели."""

    def __init__(self, name: str, accuracy: float) -> None:
        """Инициализация имени и точности модели."""
        self.name: str = name
        self.accuracy: float = accuracy


# Класс-наследник: нейросеть с оптимизатором как атрибутом
class NeuralNetwork(Model):
    """Класс нейросети, наследующий свойства от Model."""

    def __init__(self, name: str, accuracy: float, layers: int, optimizer: Optimizer) -> None:
        """Инициализация атрибутов родителя и оптимизатора."""
        super().__init__(name, accuracy)
        self.layers: int = layers
        # Экземпляр класса Optimizer сохраняется как атрибут
        self.optimizer: Optimizer = optimizer

    def describe(self) -> None:
        """Расширенное описание нейросети."""
        print(f"  Модель: {self.name}")
        print(f"  Точность: {self.accuracy}")
        print(f"  Количество слоев: {self.layers}")
        # Вызов метода экземпляра-атрибута
        self.optimizer.describe()


# Создаём экземпляр Optimizer отдельно
sgd_optimizer: Optimizer = Optimizer(0.01, "SGD")

# Передаём optimizer как аргумент при создании NeuralNetwork
print("Нейросеть с оптимизатором:")
nn_model: NeuralNetwork = NeuralNetwork("Deep CNN", 0.95, 50, sgd_optimizer)
nn_model.describe()