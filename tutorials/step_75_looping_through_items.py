"""
Микро-шаг 75: Итерация по всем парам ключ-значение (Looping Through All Key-Value Pairs).
Метод items() возвращает все пары из словаря для последовательной обработки.
В ML это используется для обхода всех параметров модели
или всех признаков (колонок данных) при их подготовке.
"""

# Метрики обученной модели
metrics: dict[str, float] = {
    'accuracy': 0.94,
    'precision': 0.91,
    'recall': 0.89,
    'f1_score': 0.90
}

print("Все метрики модели:")
# Метод items() возвращает каждую пару ключ-значение
for key, value in metrics.items():
    print(f"  {key}: {value}")

print("\nКонфигурация модели:")
model_config: dict[str, str | int] = {
    'name': 'RandomForest',
    'n_estimators': 100,
    'max_depth': 5
}

# Перебираем все пары и форматируем вывод
for parameter, setting in model_config.items():
    print(f"  {parameter} = {setting}")