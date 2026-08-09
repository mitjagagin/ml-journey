"""
Микро-шаг 73: Удаление пар ключ-значение (Removing Key-Value Pairs).
Оператор del удаляет пару из словаря по ключу.
В ML это нужно, когда из данных удаляют лишнее поле,
например пароль или признак (колонку данных), который не нужен модели.
"""

# Данные пользователя до очистки
user_data: dict[str, str | int] = {
    'name': 'Dmitry',
    'age': 30,
    'password': 'secret123'
}

print("Данные пользователя до удаления:")
print(f"  {user_data}")

# Удаляем поле password, потому что оно не должно использоваться моделью
del user_data['password']

print("\nДанные пользователя после удаления:")
print(f"  {user_data}")

# Результаты оценки модели
evaluation_results: dict[str, float] = {
    'accuracy': 0.94,
    'roc_auc': 0.91
}

print("\nМетрики до удаления:")
print(f"  {evaluation_results}")

# Удаляем временную метрику, которая больше не нужна
del evaluation_results['roc_auc']

print("\nМетрики после удаления:")
print(f"  {evaluation_results}")