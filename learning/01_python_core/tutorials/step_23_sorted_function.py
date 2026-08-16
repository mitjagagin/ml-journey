"""
Микро-шаг 23: Временная сортировка списка через sorted().
sorted(список) возвращает НОВЫЙ отсортированный список,
оригинал остаётся неизменным. Это безопаснее, чем .sort().
"""

# Исходный список моделей
ml_models: list[str] = ["XGBoost", "Random Forest", "Linear Regression", "Decision Tree"]
print(f"Исходный список: {ml_models}")

# sorted() возвращает новую отсортированную копию
sorted_models: list[str] = sorted(ml_models)
print(f"sorted(ml_models): {sorted_models}")

# ВАЖНО: исходный список НЕ изменился!
print(f"Исходный список после sorted(): {ml_models}")

# Обратный порядок через sorted(reverse=True)
sorted_reverse: list[str] = sorted(ml_models, reverse=True)
print(f"sorted(reverse=True): {sorted_reverse}")

# И снова: оригинал всё ещё нетронут
print(f"Исходный список в конце: {ml_models}")