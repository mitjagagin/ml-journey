"""
Микро-шаг 103: Возврат списка (Returning a List).
Функция фильтрует данные и возвращает список подходящих значений.
В ML это используется для отбора предсказаний с уверенностью выше порога
или фильтрации признаков (колонок данных) по заданному критерию.
"""

# Функция возвращает список значений loss ниже порога
def filter_good_losses(losses: list[float], threshold: float) -> list[float]:
    good_losses: list[float] = []
    for loss in losses:
        if loss < threshold:
            good_losses.append(loss)
    return good_losses

# Исходные данные: значения loss за 8 эпох обучения
all_losses: list[float] = [0.95, 0.82, 0.71, 0.63, 0.55, 0.48, 0.41, 0.35]

# Вызываем функцию с порогом 0.5
filtered: list[float] = filter_good_losses(all_losses, 0.5)

print("Все значения loss:")
for loss in all_losses:
    print(f"  {loss}")

print("\nЗначения loss ниже порога 0.5:")
for loss in filtered:
    print(f"  {loss}")