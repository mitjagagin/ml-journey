"""
Микро-шаг 114: Вызов методов (Calling Methods).
Вызываем методы объекта последовательно и с аргументами.
В ML это основные операции: model.fit(X), model.predict(X).
Каждый метод принимает данные как аргумент.
"""


class DataProcessor:
    """Процессор данных для ML-пайплайна."""

    def __init__(self, source: str) -> None:
        """Инициализирует процессор с источником данных."""
        self.source: str = source

    def load(self) -> None:
        """Загружает данные из источника."""
        print(f"Загрузка данных из: {self.source}")

    def clean(self) -> None:
        """Очищает данные от пропусков."""
        print("Очистка данных от пропущенных значений")

    def transform(self, batch_size: int) -> None:
        """Преобразует данные по батчам."""
        print(f"Преобразование данных батчами по {batch_size}")


# Создаём экземпляр процессора
processor: DataProcessor = DataProcessor("customer_data.csv")

# Вызываем методы последовательно — это ML-пайплайн
print("Запуск пайплайна обработки:")
processor.load()
processor.clean()

# Метод с аргументом: передаём размер батча
processor.transform(32)