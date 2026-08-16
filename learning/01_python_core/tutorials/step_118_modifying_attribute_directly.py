"""
Микро-шаг 118: Прямое изменение атрибута (Modifying an Attribute's Value Directly).
Изменяем значение атрибута через прямое присваивание.
В ML это аналогично прямой смене гиперпараметра модели перед обучением,
например model.learning_rate = 0.001. Быстро, но без валидации.
"""


class Car:
    """Простая модель автомобиля."""

    def __init__(self, make: str, model: str, year: int) -> None:
        """Инициализирует атрибуты автомобиля."""
        self.make: str = make
        self.model: str = model
        self.year: int = year
        self.odometer_reading: int = 0

    def get_descriptive_name(self) -> str:
        """Возвращает описательное имя автомобиля."""
        long_name: str = f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self) -> None:
        """Выводит пробег автомобиля."""
        print(f"  Пробег: {self.odometer_reading} миль")


# Создаём экземпляр
my_car: Car = Car("audi", "a4", 2024)

print("До изменения:")
my_car.read_odometer()

# Прямое изменение атрибута через точку
my_car.odometer_reading = 23

print("\nПосле прямого изменения:")
my_car.read_odometer()