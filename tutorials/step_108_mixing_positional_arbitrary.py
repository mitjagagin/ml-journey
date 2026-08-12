"""
Микро-шаг 108: Смешивание позиционных и произвольных аргументов
(Mixing Positional and Arbitrary Arguments).
Комбинация обязательных параметров с произвольным количеством дополнительных.
В ML это нужно для функций, где первый аргумент обязателен (имя модели),
а остальные — опциональные (дополнительные признаки).
"""

# Первый параметр model_name — обязательный (позиционный)
# Второй параметр *additional_features — произвольное количество
def describe_model(model_name: str, *additional_features: str) -> None:
    print(f"Модель: {model_name}")
    if additional_features:
        print("Дополнительные признаки:")
        for feature in additional_features:
            print(f"  - {feature}")
    else:
        print("Без дополнительных признаков")

# Только обязательный параметр
print("\nБазовая конфигурация:")
describe_model("LogisticRegression")

# Обязательный + несколько дополнительных
print("\nРасширенная конфигурация:")
describe_model("RandomForest", "возраст", "доход", "город")

# Обязательный + один дополнительный
print("\nМинимальное расширение:")
describe_model("LinearRegression", "только_доход")