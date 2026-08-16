"""
Микро-шаг 119: Изменение атрибута через метод (Modifying an Attribute's Value Through a Method).
Передаём новое значение в метод, который сам обновляет атрибут.
В ML так безопасно меняют гиперпараметры: в метод можно добавить
проверку значения перед его записью в атрибут.
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


# Создаём экземпляр
my_car: Car = Car("audi", "a4", 2024)

print("До изменения:")
my_car.read_odometer()

# Изменение через метод: передаём значение как аргумент
my_car.update_odometer(23)

print("\nПосле изменения через метод:")
my_car.read_odometer()