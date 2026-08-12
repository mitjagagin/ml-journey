"""
Микро-шаг 92: Удаление всех вхождений значения из списка (Removing All Instances).
Метод remove() удаляет только ПЕРВОЕ вхождение значения.
Чтобы удалить ВСЕ вхождения, нужно использовать цикл while,
который проверяет, есть ли еще такое значение в списке.
В ML это используется для очистки датасетов (наборов данных):
например, удалить все строки с пропущенными значениями или все
примеры определенного класса, который нужно исключить из обучения.
"""

# Список метрик (числовых оценок качества модели)
# Некоторые значения — ошибки (NaN — Not a Number, пропущенное значение)
metrics: list[str] = ["0.85", "NaN", "0.92", "NaN", "0.78", "NaN", "0.88"]

print("Исходный список метрик:")
for metric in metrics:
    print(f"  {metric}")

# Удаляем ВСЕ вхождения "NaN" из списка
# Цикл работает, пока "NaN" есть в списке
while "NaN" in metrics:
    metrics.remove("NaN")

print("\nСписок после удаления всех NaN:")
for metric in metrics:
    print(f"  {metric}")

# Еще один пример: удаление определенной модели из списка экспериментов
experiments: list[str] = ["logistic_regression", "random_forest", "logistic_regression", "svm"]

print("\nИсходный список экспериментов:")
for exp in experiments:
    print(f"  {exp}")

# Удаляем все эксперименты с logistic_regression (допустим, они не удались)
while "logistic_regression" in experiments:
    experiments.remove("logistic_regression")

print("\nСписок после удаления всех logistic_regression:")
for exp in experiments:
    print(f"  {exp}")