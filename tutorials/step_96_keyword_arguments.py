"""
Микро-шаг 96: Именованные аргументы (Keyword Arguments).
Передача аргументов по имени параметра, где порядок не важен.
В ML это используется при настройке гиперпараметров (настроек модели),
чтобы код был читаемым и не зависел от порядка аргументов.
"""

# Определяем функцию с двумя параметрами
def describe_experiment(model_name: str, dataset_name: str) -> None:
    print(f"Модель: {model_name}")
    print(f"Датасет: {dataset_name}")

# Способ 1: Позиционные аргументы (порядок важен)
print("Позиционные аргументы:")
describe_experiment("LogisticRegression", "Wine")

# Способ 2: Именованные аргументы в том же порядке
print("\nИменованные аргументы (прямой порядок):")
describe_experiment(model_name="LogisticRegression", dataset_name="Wine")

# Способ 3: Именованные аргументы в ОБРАТНОМ порядке
# Python понимает, куда что положить, по именам!
print("\nИменованные аргументы (обратный порядок):")
describe_experiment(dataset_name="Wine", model_name="LogisticRegression")