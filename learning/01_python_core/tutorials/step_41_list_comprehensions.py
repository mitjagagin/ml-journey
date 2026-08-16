"""
Микро-шаг 41 (исправленный): List Comprehensions и функция round().
Исправление артефактов плавающей запятой (например, 55.00000000000001).
В ML метрики и loss всегда округляют до 2-4 знаков для читаемости.
"""

# Исходные данные: значения loss (функции потерь) за 6 эпох
losses: list[float] = [0.85, 0.72, 0.61, 0.55, 0.48, 0.42]

# Базовый синтаксис с округлением: round(значение, количество_знаков)
# Теперь 0.55 * 100 = 55.0, а не 55.00000000000001
losses_percent: list[float] = [round(loss * 100, 2) for loss in losses]
print(f"Loss в процентах: {losses_percent}")

# List comprehension с условием: отбираем только те эпохи, где loss < 0.6
good_epochs: list[float] = [loss for loss in losses if loss < 0.6]
print(f"\nЭпохи с loss < 0.6: {good_epochs}")

# Преобразование типов: из строк в числа (например, при загрузке из CSV)
accuracy_strings: list[str] = ["85.5", "92.3", "88.1", "95.0"]
accuracy_numbers: list[float] = [float(acc) for acc in accuracy_strings]
print(f"\nТочность как числа: {accuracy_numbers}")

# Создание списка индексов для итерации
indices: list[int] = [i for i in range(len(losses))]
print(f"\nИндексы эпох: {indices}")