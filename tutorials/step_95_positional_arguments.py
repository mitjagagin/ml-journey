"""
Микро-шаг 95: Позиционные аргументы (Positional Arguments).
Передача данных в функцию, где порядок аргументов строго важен.
В ML это используется для передачи названий моделей или путей к датасетам
(наборам данных) в функции, чтобы не дублировать код для каждого эксперимента.
"""

# Определяем функцию с двумя параметрами (ожидаемыми переменными)
# : str означает, что мы ожидаем текст (строку)
def describe_experiment(model_name: str, dataset_name: str) -> None:
    print(f"Модель: {model_name}")
    print(f"Датасет: {dataset_name}")

# Вызываем функцию, передавая аргументы (реальные значения)
# Python берет первый аргумент и кладет его в model_name, второй - в dataset_name
print("Первый эксперимент:")
describe_experiment("LogisticRegression", "Wine")

print("\nВторой эксперимент:")
describe_experiment("RandomForest", "Titanic")

# Что будет, если перепутать порядок при вызове?
print("\nЭксперимент с перепутанным порядком (ошибка логики):")
describe_experiment("HousePrices", "LinearRegression")