"""
Микро-шаг 33: Создание числового списка через list(range(...)).
Функция list() преобразует объект range в полноценный список,
который можно хранить, индексировать и передавать в ML-функции.
"""

# 1. Создаём список эпох от 1 до 5
epochs: list[int] = list(range(1, 6))
print(f"Список эпох: {epochs}")
print(f"Тип: {type(epochs).__name__}")

# 2. Создаём список чётных чисел от 0 до 20 (шаг 2)
even_numbers: list[int] = list(range(0, 21, 2))
print(f"\nЧётные числа: {even_numbers}")

# 3. Создаём список индексов для батчей (10 батчей)
batch_indices: list[int] = list(range(10))
print(f"\nИндексы батчей: {batch_indices}")
print(f"Количество батчей: {len(batch_indices)}")

# 4. ВАЖНО: разница между range и list
lazy_range = range(5)          # "ленивый" объект, не хранит числа
eager_list: list[int] = list(range(5))  # полноценный список в памяти
print(f"\ntype(range(5)) = {type(lazy_range).__name__}")
print(f"type(list(range(5))) = {type(eager_list).__name__}")