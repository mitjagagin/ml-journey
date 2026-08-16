"""
Микро-шаг 72: Изменение значений в словаре (Modifying Values in a Dictionary).
Изменение значения по ключу с использованием условий для определения нового значения.
В ML это используется для обновления статуса модели или её параметров
в зависимости от результатов обучения или проверки качества.
"""

# Словарь с текущим статусом модели и её метрикой
model_state: dict[str, str | float] = {
    'name': 'LogisticRegression',
    'status': 'training',
    'accuracy': 0.85
}

print("Состояние модели до проверки:")
print(f"  {model_state}")

# Изменяем статус в зависимости от точности
# Порог для продакшена (готовности к использованию)
production_threshold: float = 0.90

if model_state['accuracy'] >= production_threshold:
    model_state['status'] = 'ready_for_production'
else:
    model_state['status'] = 'needs_improvement'

print("\nСостояние модели после проверки:")
print(f"  {model_state}")

# Ещё один пример: изменение гиперпараметра (настройки модели) на основе эпохи (прогона по данным)
training_config: dict[str, int | float] = {
    'learning_rate': 0.1,
    'current_epoch': 5
}

print("\nКонфигурация обучения до обновления:")
print(f"  {training_config}")

# Уменьшаем learning_rate (скорость обучения) после 5-й эпохи
if training_config['current_epoch'] == 5:
    training_config['learning_rate'] = 0.01

print("\nКонфигурация обучения после обновления:")
print(f"  {training_config}")