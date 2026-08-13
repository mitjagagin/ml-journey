"""
Микро-шаг 112: Создание экземпляра класса (Making an Instance from a Class).
Разбираем процесс инстанцирования — создания объекта из класса.
В ML это аналогично созданию модели с настройками:
model = LogisticRegression(C=1.0) — вызываем класс, получаем объект.
"""


class Pipeline:
    """ML-пайплайн (последовательность шагов обработки данных)."""

    def __init__(self, name: str, steps: int) -> None:
        """Инициализирует пайплайн."""
        self.name: str = name
        self.steps: int = steps


# Инстанцирование: вызываем класс как функцию.
# Python читает эту строку и делает три вещи:
# 1. Создаёт новый пустой объект класса Pipeline
# 2. Вызывает __init__, передавая "data_cleaning" и 3
# 3. Сохраняет готовый объект в переменную my_pipeline
my_pipeline: Pipeline = Pipeline("data_cleaning", 3)

# Результат — готовый объект с атрибутами
print("Экземпляр пайплайна создан:")
print(f"  Название: {my_pipeline.name}")
print(f"  Количество шагов: {my_pipeline.steps}")