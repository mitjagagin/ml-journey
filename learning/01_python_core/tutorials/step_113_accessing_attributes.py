"""
Микро-шаг 113: Доступ к атрибутам (Accessing Attributes).
Используем атрибуты объекта в переменных, условиях и выражениях.
В ML это нужно для чтения гиперпараметров модели при логировании:
например, записать config.learning_rate в систему трекинга экспериментов.
"""


class ModelConfig:
    """Конфигурация модели (набор гиперпараметров)."""

    def __init__(self, algorithm: str, learning_rate: float, epochs: int) -> None:
        """Инициализирует гиперпараметры."""
        self.algorithm: str = algorithm
        self.learning_rate: float = learning_rate
        self.epochs: int = epochs


# Создаём экземпляр с настройками
config: ModelConfig = ModelConfig("SGD", 0.01, 50)

# Доступ к атрибутам через точечную нотацию
print("Гиперпараметры модели:")
print(f"  Алгоритм: {config.algorithm}")
print(f"  Learning rate: {config.learning_rate}")
print(f"  Эпохи: {config.epochs}")

# Атрибут можно сохранить в обычную переменную
lr: float = config.learning_rate
print(f"\nСохранено в переменную: lr = {lr}")

# Атрибут можно использовать в условии
if config.epochs > 30:
    print("Долгое обучение: больше 30 эпох")
else:
    print("Быстрое обучение: 30 эпох или меньше")