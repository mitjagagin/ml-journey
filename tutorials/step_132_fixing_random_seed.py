"""
Микро-шаг 132: Фиксация seed для воспроизводимости (Fixing Random Seed).
Фиксация зерна генератора случайных чисел для получения одинаковых результатов.
В ML это критически важно: без seed невозможно воспроизвести эксперимент,
отладить модель или сравнить два алгоритма на одних и тех же данных.
"""

# Импорт стандартного модуля random
import random

print("БЕЗ фиксации seed (результат разный при каждом запуске):")
for i in range(1, 4):
    random_number: int = random.randint(1, 100)
    print(f"  Число {i}: {random_number}")

print("\nС фиксацией seed=42 (результат одинаковый при каждом запуске):")
# Фиксация seed перед генерацией случайных чисел
random.seed(42)
for i in range(1, 4):
    random_number: int = random.randint(1, 100)
    print(f"  Число {i}: {random_number}")

print("\nПовторная фиксация того же seed (те же самые числа):")
random.seed(42)
for i in range(1, 4):
    random_number: int = random.randint(1, 100)
    print(f"  Число {i}: {random_number}")

print("\nДругой seed (другая последовательность):")
random.seed(123)
for i in range(1, 4):
    random_number: int = random.randint(1, 100)
    print(f"  Число {i}: {random_number}")

# Практический пример из ML: воспроизводимое разбиение данных
print("\nВоспроизводимое разбиение датасета на train/test:")
dataset_size: int = 100
random.seed(42)
train_indices: list[int] = random.sample(range(dataset_size), 80)

# Собираем test_indices: все индексы, которых нет в train
test_indices: list[int] = [i for i in range(dataset_size) if i not in train_indices]

print(f"  Train размер: {len(train_indices)}")
print(f"  Test размер: {len(test_indices)}")
print(f"  Первые 5 train индексов: {train_indices[:5]}")