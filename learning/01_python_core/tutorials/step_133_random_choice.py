"""
Микро-шаг 133: Выбор случайного элемента из списка (random.choice).
Использование random.choice() для выбора одного случайного элемента из последовательности.
В ML это используется для выбора случайного примера из датасета (набора данных),
случайного класса для предсказания или случайного гиперпараметра из списка возможных.
"""

# Импорт стандартного модуля random
import random

print("Выбор случайного элемента из списка:")

# Список названий моделей
models: list[str] = ["Logistic Regression", "Random Forest", "SVM", "Neural Network"]

# Выбор одной случайной модели
chosen_model: str = random.choice(models)
print(f"  Выбранная модель: {chosen_model}")

# Выбор случайного гиперпараметра (настройки модели)
print("\nВыбор случайного гиперпараметра:")
learning_rates: list[float] = [0.001, 0.01, 0.1, 1.0]
chosen_lr: float = random.choice(learning_rates)
print(f"  Выбранная скорость обучения: {chosen_lr}")

# Выбор случайного класса для многоклассовой классификации
print("\nВыбор случайного класса:")
classes: list[str] = ["cat", "dog", "bird", "fish", "horse"]
chosen_class: str = random.choice(classes)
print(f"  Выбранный класс: {chosen_class}")

# Практический пример с фиксацией seed для воспроизводимости
print("\nВоспроизводимый выбор (с фиксацией seed):")
random.seed(42)
for i in range(1, 6):
    random_model: str = random.choice(models)
    print(f"  Итерация {i}: {random_model}")

print("\nПовторный запуск с тем же seed (те же результаты):")
random.seed(42)
for i in range(1, 6):
    random_model: str = random.choice(models)
    print(f"  Итерация {i}: {random_model}")

# Выбор случайного элемента из range()
print("\nВыбор случайного индекса из диапазона:")
dataset_size: int = 1000
random_index: int = random.choice(range(dataset_size))
print(f"  Случайный индекс: {random_index}")