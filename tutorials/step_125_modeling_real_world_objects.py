"""
Микро-шаг 125: Моделирование реальных объектов (Modeling Real-World Objects).
Процесс мышления при моделировании: какие атрибуты, методы и связи нужны.
В ML это ключевой навык: перед написанием кода нужно продумать, как представить
данные, эксперименты и модели в виде классов и их взаимодействий.
"""


# ЭТАП 1 моделирования: Определяем объекты предметной области.
# Вопрос: "Какие сущности мне нужны?"
# Ответ: Датасет (набор данных) и Эксперимент обучения (TrainingRun).


# ЭТАП 2 моделирования: Определяем атрибуты каждого объекта.
# Вопрос: "Какую информацию должен хранить объект?"
class Dataset:
    """Датасет (набор данных) для обучения модели."""

    def __init__(self, name: str, num_rows: int, num_features: int) -> None:
        """Инициализация имени, количества строк и количества признаков."""
        self.name: str = name
        self.num_rows: int = num_rows
        self.num_features: int = num_features

    # ЭТАП 3 моделирования: Определяем методы (поведение) объекта.
    # Вопрос: "Что должен уметь делать объект?"
    def describe(self) -> None:
        """Вывод описания датасета."""
        print(f"  Датасет: {self.name}")
        print(f"  Строк: {self.num_rows}")
        print(f"  Признаков: {self.num_features}")


class TrainingRun:
    """Эксперимент обучения модели на датасете."""

    def __init__(self, run_name: str, dataset: Dataset, epochs: int) -> None:
        """Инициализация имени эксперимента, датасета и числа эпох."""
        self.run_name: str = run_name
        # ЭТАП 4 моделирования: Определяем связи между объектами (композиция).
        # Вопрос: "Как объекты связаны друг с другом?"
        self.dataset: Dataset = dataset
        self.epochs: int = epochs

    def describe(self) -> None:
        """Вывод описания эксперимента обучения."""
        print(f"Эксперимент: {self.run_name}")
        print(f"Эпох обучения: {self.epochs}")
        print("Датасет:")
        self.dataset.describe()


# Создаём объекты и связываем их
print("Моделирование эксперимента обучения:")
iris_data: Dataset = Dataset("Iris", 150, 4)
experiment_1: TrainingRun = TrainingRun("baseline_run", iris_data, 10)
experiment_1.describe()