"""
Микро-шаг 43: Slicing — работа с частью списка.
Извлечение подмножества элементов с помощью синтаксиса [start:stop].
В ML это используется для разделения данных на train/test,
извлечения батчей и работы с временными рядами.
"""

# Датасет: значения accuracy за 10 эпох обучения
accuracies: list[float] = [72.5, 75.3, 78.1, 80.4, 82.7, 84.2, 86.5, 88.1, 89.7, 91.0]

# Базовый синтаксис: список[start:stop]
# stop — индекс, до которого извлекаем (НЕ включая его)
# Извлекаем первые 7 эпох для train set
train_accuracies: list[float] = accuracies[0:7]
print(f"Train set (эпохи 0-6): {train_accuracies}")

# Извлекаем последние 3 эпохи для test set
test_accuracies: list[float] = accuracies[7:10]
print(f"Test set (эпохи 7-9): {test_accuracies}")

# Если не указать start — срез начинается с начала списка
first_five: list[float] = accuracies[:5]
print(f"\nПервые 5 эпох: {first_five}")

# Если не указать stop — срез идёт до конца списка
last_three: list[float] = accuracies[-3:]
print(f"Последние 3 эпохи: {last_three}")

# Отрицательные индексы в slicing
# Извлекаем эпохи с 3-й по предпоследнюю
middle_epochs: list[float] = accuracies[3:-1]
print(f"\nЭпохи с 3-й по предпоследнюю: {middle_epochs}")

# Копирование списка через slicing (важно для ML-пайплайнов)
# Создаём независимую копию, чтобы не изменять оригинал
accuracies_copy: list[float] = accuracies[:]
print(f"\nКопия списка: {accuracies_copy}")

# Изменяем копию — оригинал остаётся нетронутым
accuracies_copy[0] = 99.9
print(f"Оригинал после изменения копии: {accuracies[0]}")
print(f"Копия после изменения: {accuracies_copy[0]}")