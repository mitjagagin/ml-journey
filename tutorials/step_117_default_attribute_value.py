"""
Микро-шаг 117: Атрибут со значением по умолчанию (Setting a Default Value for an Attribute).
Атрибут, который инициализируется внутри __init__ без внешнего параметра.
В ML так хранят внутреннее состояние: счётчик эпох, статус обучения,
флаг завершённости — то, что начинается с нуля или значения по умолчанию.
"""


class Car:
    """Простая модель автомобиля."""

    def __init__(self, make: str, model: str, year: int) -> None:
        """Инициализирует атрибуты автомобиля."""
        self.make: str = make
        self.model: str = model
        self.year: int = year
        # Атрибут со значением по умолчанию — не передаётся снаружи
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

# Описание автомобиля
description: str = my_car.get_descriptive_name()
print("Описание автомобиля:")
print(f"  {description.title()}")

# Обращение к атрибуту по умолчанию через метод
print("Показания одометра:")
my_car.read_odometer()