"""
Микро-шаг 21: Удаление элементов из списка.
- del список[индекс] — удаляет элемент по индексу навсегда.
- список.pop() — удаляет и возвращает последний элемент (или по индексу).
- список.remove(значение) — удаляет первое вхождение значения.
"""

# Исходный список моделей
ml_models: list[str] = ["Linear Regression", "Random Forest", "XGBoost", "Neural Network"]
print(f"Исходный список: {ml_models}")

# 1. Удаление по индексу с помощью del
del ml_models[0]  # Удаляем "Linear Regression"
print(f"После del ml_models[0]: {ml_models}")

# 2. Удаление последнего элемента с pop() и использование удаленного значения
removed_model: str = ml_models.pop()
print(f"После pop(): {ml_models}")
print(f"Удаленная модель (используется для инференса): {removed_model}")

# 3. Удаление по значению с remove()
ml_models.remove("Random Forest")
print(f"После remove('Random Forest'): {ml_models}")