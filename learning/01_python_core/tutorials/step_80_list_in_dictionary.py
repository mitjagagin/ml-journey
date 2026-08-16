"""
Микро-шаг 80: Список в словаре (A List in a Dictionary).
Словарь может содержать список как значение.
В ML это используется для хранения списка признаков (колонок данных) модели
или истории значений метрик по нескольким запускам.
"""

# Конфигурация модели со списком признаков (колонок данных)
model_config: dict[str, str | list[str]] = {
    'model_type': 'RandomForest',
    'features': ['age', 'income', 'credit_score']
}

print("Конфигурация модели:")
print(f"  Тип модели: {model_config['model_type']}")
print(f"  Признаки: {model_config['features']}")

print("\nПеребор признаков модели:")
for feature in model_config['features']:
    print(f"  {feature}")

# Доступ к конкретному признаку по индексу
first_feature: str = model_config['features'][0]
print(f"\nПервый признак: {first_feature}")

# Добавляем новый признак в список внутри словаря
model_config['features'].append('employment_years')

print("\nПризнаки после добавления нового:")
for feature in model_config['features']:
    print(f"  {feature}")

# История метрик по нескольким запускам обучения
training_history: dict[str, list[float]] = {
    'accuracy': [0.88, 0.92, 0.94],
    'loss': [0.45, 0.30, 0.22]
}

print("\nИстория обучения:")
for metric_name, values in training_history.items():
    print(f"  {metric_name}: {values}")