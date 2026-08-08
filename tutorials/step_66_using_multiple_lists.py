"""
Микро-шаг 66: Использование нескольких списков (Using Multiple Lists).
Итерация по одному списку с проверкой наличия элементов в другом списке.
В ML это используется для фильтрации признаков (features),
очистки текста от стоп-слов или проверки валидности категорий.
"""

# Список одобренных признаков для обучения модели (approved features)
approved_features: list[str] = ['age', 'income', 'education', 'credit_score']

# Список всех признаков, найденных в сыром датасете
dataset_features: list[str] = ['age', 'income', 'social_security_number', 'education', 'random_id']

print("Проверка признаков для модели:")
# Итерируем по признакам из датасета
for feature in dataset_features:
    # Проверяем, есть ли текущий признак в списке одобренных
    if feature in approved_features:
        print(f"  Добавляем признак: {feature}")
    else:
        print(f"  Исключаем признак: {feature} (нет в одобренных)")