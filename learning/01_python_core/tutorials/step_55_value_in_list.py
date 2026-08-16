"""
Микро-шаг 55: Проверка значения в списке (Value in List).
Оператор in проверяет, содержится ли элемент в списке.
В ML это используется для валидации категориальных признаков датасета
и проверки, входит ли метка класса в допустимый набор значений.
"""

# Допустимые типы моделей в проекте
allowed_models: list[str] = ["linear", "forest", "boosting", "neural"]

# Модель для проверки
model_to_check: str = "forest"

# Проверка через in
print("Проверка наличия модели в списке:")
if model_to_check in allowed_models:
    print(f"  Модель '{model_to_check}' разрешена")
else:
    print(f"  Модель '{model_to_check}' запрещена")

# Модель, которой нет в списке
unknown_model: str = "svm"

print("\nПроверка отсутствующей модели:")
if unknown_model in allowed_models:
    print(f"  Модель '{unknown_model}' разрешена")
else:
    print(f"  Модель '{unknown_model}' запрещена")

# Допустимые категории признака в датасете
valid_categories: list[str] = ["cat", "dog", "bird"]
input_category: str = "cat"

print("\nВалидация категории признака:")
if input_category in valid_categories:
    print(f"  Категория '{input_category}' валидна")
else:
    print(f"  Категория '{input_category}' невалидна")