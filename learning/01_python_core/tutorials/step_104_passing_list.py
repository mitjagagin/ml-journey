"""
Микро-шаг 104: Передача списка в функцию (Passing a List).
Список передаётся как аргумент и обрабатывается внутри функции.
В ML это используется для обработки наборов значений: метрик по эпохам,
предсказаний модели или списка признаков (колонок данных).
"""

# Функция принимает список значений loss и порог, возвращает количество
# эпох, в которых loss опустился ниже порога
def count_converged_epochs(losses: list[float], threshold: float) -> int:
    count: int = 0
    for loss in losses:
        if loss < threshold:
            count = count + 1
    return count

# Значения loss за 8 эпох обучения модели
training_losses: list[float] = [0.95, 0.82, 0.71, 0.63, 0.55, 0.48, 0.41, 0.35]

# Передаём список в функцию
converged: int = count_converged_epochs(training_losses, 0.5)

print("Значения loss по эпохам:")
for loss in training_losses:
    print(f"  {loss}")

print(f"\nЭпох с loss ниже 0.5: {converged}")