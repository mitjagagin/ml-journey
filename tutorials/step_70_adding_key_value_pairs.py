"""
Микро-шаг 70: Добавление новых пар ключ-значение (Adding New Key-Value Pairs).
Словари динамичны: новые пары можно добавлять в любой момент через dict[key] = value.
В ML это используется для добавления новых гиперпараметров в конфиг,
расширения метаданных модели и накопления результатов эксперимента.
"""

# Базовая конфигурация модели на старте
model_config: dict[str, float | int | str] = {
    'model_type': 'LogisticRegression',
    'learning_rate': 0.01
}

print("Конфигурация на старте:")
print(f"  Тип модели: {model_config['model_type']}")
print(f"  Learning rate: {model_config['learning_rate']}")

# Добавляем новые пары ключ-значение по мере необходимости
model_config['max_iterations'] = 100
model_config['regularization'] = 'l2'
model_config['random_state'] = 42

print("\nКонфигурация после добавления гиперпараметров:")
print(f"  Max iterations: {model_config['max_iterations']}")
print(f"  Regularization: {model_config['regularization']}")
print(f"  Random state: {model_config['random_state']}")

# Добавляем новую метрику в словарь с результатами оценки
evaluation: dict[str, float] = {
    'accuracy': 0.94
}

print("\nМетрики до добавления F1:")
print(f"  {evaluation}")

evaluation['f1_score'] = 0.90

print("\nМетрики после добавления F1:")
print(f"  {evaluation}")