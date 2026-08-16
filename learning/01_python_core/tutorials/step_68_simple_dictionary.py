"""
Микро-шаг 68: Простой словарь (A Simple Dictionary).
Базовая структура данных "ключ: значение" для хранения связанных данных.
В ML словари используются для хранения гиперпараметров моделей,
конфигураций экспериментов, JSON-ответов API и маппинга категорий.
"""

# Словарь с характеристиками обученной модели
model_info: dict[str, str | float] = {
    'name': 'RandomForest',
    'accuracy': 0.92,
    'version': '1.0',
    'status': 'training'
}

# Доступ к значениям по ключу
print("Информация о модели:")
print(f"  Название: {model_info['name']}")
print(f"  Accuracy: {model_info['accuracy']}")
print(f"  Версия: {model_info['version']}")
print(f"  Статус: {model_info['status']}")

# Изменение значения по ключу
model_info['status'] = 'deployed'
print("\nПосле деплоя:")
print(f"  Новый статус: {model_info['status']}")