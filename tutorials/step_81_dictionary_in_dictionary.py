"""
Микро-шаг 81: Словарь в словаре (A Dictionary in a Dictionary).
Словарь, значениями которого являются другие словари.
В ML это используется для хранения конфигов (файлов с настройками) моделей,
где каждая секция имеет свои подразделы.
"""

# Конфигурация модели с вложенными словарями
model_config: dict[str, dict[str, float | int | str]] = {
    'training': {
        'learning_rate': 0.01,
        'epochs': 100,
        'batch_size': 32
    },
    'model': {
        'type': 'RandomForest',
        'n_estimators': 100,
        'max_depth': 5
    }
}

print("Полный конфиг модели:")
print(f"  {model_config}")

print("\nДоступ к секции обучения:")
training_params: dict[str, float | int] = model_config['training']
print(f"  {training_params}")

print("\nДоступ к конкретному параметру обучения:")
learning_rate: float = model_config['training']['learning_rate']
print(f"  Learning rate: {learning_rate}")

# Добавляем новый параметр во вложенный словарь
model_config['training']['optimizer'] = 'Adam'

print("\nСекция обучения после добавления оптимизатора:")
for param, value in model_config['training'].items():
    print(f"  {param}: {value}")

# Добавляем новую секцию с подпараметрами
model_config['evaluation'] = {
    'metric': 'accuracy',
    'threshold': 0.90
}

print("\nКонфиг после добавления секции оценки:")
for section, params in model_config.items():
    print(f"  Секция '{section}':")
    for key, value in params.items():
        print(f"    {key}: {value}")