"""
Микро-шаг 20: Добавление элементов в список.
Метод .append() добавляет элемент в конец списка.
Метод .insert(индекс, элемент) вставляет элемент на конкретную позицию.
В ML это используется для добавления новых моделей, признаков или классов.
"""

# Исходный список моделей
ml_models: list[str] = ["Linear Regression", "Random Forest"]

print(f"Исходный список: {ml_models}")

# Добавляем модель в конец списка
ml_models.append("XGBoost")
print(f"После append('XGBoost'): {ml_models}")

# Вставляем модель на вторую позицию (индекс 1)
ml_models.insert(1, "Decision Tree")
print(f"После insert(1, 'Decision Tree'): {ml_models}")