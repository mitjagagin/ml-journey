"""
Микро-шаг 115: Создание нескольких экземпляров (Creating Multiple Instances).
Создаём независимые объекты одного класса.
В ML это нужно для сравнения конфигураций моделей:
каждая конфигурация хранит свои гиперпараметры независимо.
"""


class ModelConfig:
    """Конфигурация модели."""

    def __init__(self, algorithm: str, learning_rate: float, epochs: int) -> None:
        """Инициализирует конфигурацию."""
        self.algorithm: str = algorithm
        self.learning_rate: float = learning_rate
        self.epochs: int = epochs

    def describe(self) -> None:
        """Выводит описание конфигурации."""
        print(f"  Алгоритм: {self.algorithm}, lr: {self.learning_rate}, эпохи: {self.epochs}")


# Создаём три независимые конфигурации из одного класса
config_baseline: ModelConfig = ModelConfig("LogisticRegression", 0.01, 50)
config_candidate: ModelConfig = ModelConfig("RandomForest", 0.1, 100)
config_aggressive: ModelConfig = ModelConfig("NeuralNetwork", 0.001, 200)

print("Конфигурация baseline:")
config_baseline.describe()

print("\nКонфигурация candidate:")
config_candidate.describe()

print("\nКонфигурация aggressive:")
config_aggressive.describe()

# Каждый объект хранит свои данные независимо
print("\nПрямой доступ к атрибутам:")
print(f"  baseline lr: {config_baseline.learning_rate}")
print(f"  candidate lr: {config_candidate.learning_rate}")
print(f"  aggressive lr: {config_aggressive.learning_rate}")