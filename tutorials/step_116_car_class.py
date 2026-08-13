"""
Микро-шаг 116: Класс Car (The Car Class).
Создаём класс с методом, который возвращает значение.
В ML такие методы используются для описания модели
и формирования имени артефакта (файла с сохранённой моделью).
"""


class Car:
    """Простая модель автомобиля."""

    def __init__(self, make: str, model: str, year: int) -> None:
        """Инициализирует атрибуты автомобиля."""
        self.make: str = make
        self.model: str = model
        self.year: int = year

    def get_descriptive_name(self) -> str:
        """Возвращает описательное имя автомобиля."""
        long_name: str = f"{self.year} {self.make} {self.model}"
        return long_name


# Создаём экземпляр
my_car: Car = Car("audi", "a4", 2024)

# Метод возвращает строку — сохраняем её в переменную
description: str = my_car.get_descriptive_name()

print("Описание автомобиля:")
print(f"  {description.title()}")