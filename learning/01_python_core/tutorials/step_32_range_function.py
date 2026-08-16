"""
Микро-шаг 32: Функция range() для генерации числовых последовательностей.
range() создаёт последовательность чисел, которую можно перебрать циклом for.
"""

print("=== Пример 1: range(5) — числа от 0 до 4 ===")
# range(5) генерирует числа: 0, 1, 2, 3, 4 (не включая 5)
for i in range(5):
    print(f"Эпоха {i}")

print("\n=== Пример 2: range(1, 6) — числа от 1 до 5 ===")
# range(start, stop) — start включается, stop НЕ включается
for epoch in range(1, 6):
    print(f"Эпоха обучения: {epoch}")

print("\n=== Пример 3: range(0, 10, 2) — чётные числа от 0 до 8 ===")
# range(start, stop, step) — step задаёт шаг
for batch_idx in range(0, 10, 2):
    print(f"Индекс батча: {batch_idx}")

print("\n=== Пример 4: range(10, 0, -2) — обратный порядок ===")
# Отрицательный step для обратного отсчёта
for countdown in range(10, -2, -2):
    print(f"Обратный отсчёт: {countdown}")