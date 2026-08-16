# src/step_04_variables_are_labels.py
"""Демонстрация концепции: переменные — это ярлыки, а не коробки."""

# 1. Создаём объект 0.85 и вешаем на него ярлык 'model_accuracy'
# ': float' — это type hint (подсказка типа). Python его игнорирует при запуске,
# но он помогает IDE и другим разработчикам понимать код.
model_accuracy: float = 0.85
print(f"Initial accuracy: {model_accuracy}")

# 2. Переназначаем переменную.
# Мы не меняем число 0.85. Мы просто переклеиваем ярлык 'model_accuracy'
# на новый объект 0.92 (как будто мы дообучили модель).
model_accuracy = 0.92
print(f"Updated accuracy: {model_accuracy}")

# 3. Проверка через id(). Функция id() показывает уникальный адрес объекта в памяти.
# Это доказывает, что мы работаем с разными объектами.
print(f"ID of 0.85 (if we check it): {id(0.85)}")
print(f"Current ID of model_accuracy: {id(model_accuracy)}")