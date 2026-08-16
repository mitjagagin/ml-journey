"""
Микро-шаг 78: Итерация по ключам словаря в определённом порядке (Looping Through Keys in Order).
Функция sorted() возвращает ключи словаря в отсортированном порядке.
В ML это используется для вывода результатов эксперимента
или логирования метрик в предсказуемом алфавитном порядке.
"""

# Метрики модели, добавленные в произвольном порядке
metrics: dict[str, float] = {
    'f1_score': 0.90,
    'accuracy': 0.94,
    'recall': 0.89,
    'precision': 0.91
}

print("Метрики в порядке добавления:")
for key in metrics.keys():
    print(f"  {key}: {metrics[key]}")

print("\nМетрики в алфавитном порядке:")
for key in sorted(metrics.keys()):
    print(f"  {key}: {metrics[key]}")

# Участники проекта
team_members: dict[str, str] = {
    'Dmitry': 'ML Engineer',
    'Alice': 'Data Scientist',
    'Bob': 'DevOps Engineer',
    'Carol': 'Product Manager'
}

print("\nУчастники проекта по алфавиту:")
for name in sorted(team_members.keys()):
    print(f"  {name}: {team_members[name]}")