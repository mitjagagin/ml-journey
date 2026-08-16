"""
Микро-шаг 45: Итерация по части списка (Looping Through a Slice).
Цикл for по срезу списка для обработки подмножества данных.
В ML это используется для анализа подмножеств датасета,
проверки части предсказаний или работы с train/test split.
"""

# Датасет: значения loss за 10 эпох обучения
losses: list[float] = [0.95, 0.87, 0.78, 0.69, 0.61, 0.54, 0.48, 0.43, 0.39, 0.36]

# Итерация по первым 5 эпохам (начало обучения)
print("Первые 5 эпох (начало обучения):")
for loss in losses[:5]:
    print(f"  Loss: {loss}")

# Итерация по последним 3 эпохам (конец обучения, модель сходится)
print("\nПоследние 3 эпохи (конец обучения):")
for loss in losses[-3:]:
    print(f"  Loss: {loss}")

# Итерация по срезу в середине (эпохи 2-7)
print("\nЭпохи 2-7 (середина обучения):")
for loss in losses[2:8]:
    print(f"  Loss: {loss}")

# Практический пример: анализ train/test split
# Разделяем данные на train (первые 7) и test (последние 3)
train_losses: list[float] = losses[:7]
test_losses: list[float] = losses[-3:]

print("\nTrain set:")
for loss in train_losses:
    print(f"  {loss}")

print("\nTest set:")
for loss in test_losses:
    print(f"  {loss}")