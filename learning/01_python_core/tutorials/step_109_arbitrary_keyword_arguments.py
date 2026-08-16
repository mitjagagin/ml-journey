"""
Микро-шаг 109: Произвольные именованные аргументы (Arbitrary Keyword Arguments).
Использование двойной звёздочки (**) для приёма любого числа именованных аргументов.
В ML это нужно для гибкой настройки гиперпараметров (настроек модели):
функция принимает любое количество пар имя=значение без жёсткой привязки.
"""

# Двойная звёздочка перед именем собирает все именованные аргументы в словарь
def configure_experiment(model_name: str, **hyperparams: float) -> None:
    print(f"Модель: {model_name}")
    if hyperparams:
        print("Гиперпараметры:")
        for param, value in hyperparams.items():
            print(f"  {param}: {value}")
    else:
        print("Гиперпараметры не заданы (используются значения по умолчанию)")

# Вызов без дополнительных параметров
print("\nБазовая конфигурация:")
configure_experiment("LogisticRegression")

# Вызов с двумя гиперпараметрами
print("\nСтандартная конфигурация:")
configure_experiment("RandomForest", learning_rate=0.01, epochs=100.0)

# Вызов с четырьмя гиперпараметрами
print("\nПолная конфигурация:")
configure_experiment(
    "NeuralNetwork",
    learning_rate=0.001,
    epochs=500.0,
    batch_size=32.0,
    dropout=0.2
)