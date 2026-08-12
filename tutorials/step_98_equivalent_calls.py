"""
Микро-шаг 98: Эквивалентные вызовы функций (Equivalent Function Calls).
Разные способы вызова одной функции с одинаковым результатом.
В ML это позволяет гибко настраивать гиперпараметры (настройки модели),
комбинируя позиционные и именованные аргументы для читаемости.
"""

# Функция с двумя обязательными параметрами и одним по умолчанию
def describe_experiment(model_name: str, dataset_name: str, epochs: int = 10) -> None:
    print(f"Модель: {model_name}")
    print(f"Датасет: {dataset_name}")
    print(f"Эпохи: {epochs}")

# Способ 1: Только позиционные аргументы
print("Способ 1: Позиционные аргументы")
describe_experiment("LogisticRegression", "Wine", 20)

# Способ 2: Позиционные + именованный аргумент
print("\nСпособ 2: Позиционные + именованный")
describe_experiment("LogisticRegression", "Wine", epochs=20)

# Способ 3: Все именованные аргументы
print("\nСпособ 3: Все именованные")
describe_experiment(model_name="LogisticRegression", dataset_name="Wine", epochs=20)