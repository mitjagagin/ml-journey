"""
Микро-шаг 22: Постоянная сортировка списка.
Метод .sort() изменяет список навсегда (in-place).
Параметр reverse=True сортирует в обратном порядке.
В ML используется для ранжирования моделей по метрикам или признаков по важности.
"""

# Список моделей в случайном порядке
ml_models: list[str] = ["XGBoost", "Random Forest", "Linear Regression", "Decision Tree"]
print(f"Исходный список: {ml_models}")

# Сортировка в алфавитном порядке (A-Z)
ml_models.sort()
print(f"После sort() (алфавитный порядок): {ml_models}")

# Сортировка в обратном порядке (Z-A)
ml_models.sort(reverse=True)
print(f"После sort(reverse=True) (обратный порядок): {ml_models}")