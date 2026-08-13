"""
Микро-шаг 110: Создание класса Dog (Creating the Dog Class).
Создаем первый класс с атрибутами и методами.
В ML классы используются для создания моделей, конфигов и структур данных.
"""


class Dog:
    """Простая модель собаки."""

    def __init__(self, name: str, age: int) -> None:
        """Инициализирует атрибуты name и age."""
        self.name: str = name
        self.age: int = age

    def sit(self) -> None:
        """Моделирует команду 'сидеть'."""
        print(f"{self.name} is now sitting.")

    def roll_over(self) -> None:
        """Моделирует команду 'перевернуться'."""
        print(f"{self.name} rolled over!")


# Создаем экземпляр класса (конкретный объект)
my_dog: Dog = Dog("Willie", 6)

# Обращаемся к атрибутам через точку
print("Атрибуты собаки:")
print(f"  Имя: {my_dog.name}")
print(f"  Возраст: {my_dog.age} лет")

# Вызываем методы объекта
print("\nКоманды:")
my_dog.sit()
my_dog.roll_over()