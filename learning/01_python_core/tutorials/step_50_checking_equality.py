"""
Микро-шаг 50: Проверка равенства (Checking for Equality).
Оператор == возвращает True или False как обычное значение,
которое можно вывести или сохранить. Сравнение строк чувствительно к регистру.
В ML это используется при сравнении предсказанных меток с истинными,
при проверке статуса модели и валидации типов данных.
"""

# Модель, которую мы ожидаем получить
expected_model: str = "linear_regression"

# Проверка: совпадает ли ожидаемая модель с эталонным значением
print("Проверка равенства строк:")
print(f"  expected_model == 'linear_regression': {expected_model == 'linear_regression'}")
print(f"  expected_model == 'random_forest': {expected_model == 'random_forest'}")

# Проверка с другим регистром (регистр важен!)
print("\nПроверка с другим регистром:")
print(f"  expected_model == 'LINEAR_REGRESSION': {expected_model == 'LINEAR_REGRESSION'}")