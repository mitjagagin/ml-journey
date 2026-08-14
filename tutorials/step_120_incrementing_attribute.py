"""
Микро-шаг 120: Увеличение атрибута через метод (Incrementing an Attribute's Value Through a Method).
Увеличиваем значение атрибута на заданную величину.
В ML это аналогично увеличению счётчика эпох при обучении:
после каждой эпохи счётчик увеличивается на 1.
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

    def update_odometer(self, odometer_reading: int) -> None:
        """Устанавливает пробег в заданное значение."""
        self.odometer_reading = odometer_reading

    def increment_odometer(self, miles: int) -> None:
        """Увеличивает пробег на заданное количество миль."""
        self.odometer_reading += miles


# Создаём экземпляр
my_car: Car = Car("audi", "a4", 2024)

print("Начальный пробег:")
my_car.read_odometer()

# Увеличиваем пробег на 100 миль
my_car.increment_odometer(100)
print("\nПосле первой поездки (+100 миль):")
my_car.read_odometer()

# Увеличиваем пробег ещё на 50 миль
my_car.increment_odometer(50)
print("\nПосле второй поездки (+50 миль):")
my_car.read_odometer()