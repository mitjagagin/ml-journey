"""
Микро-шаг 38: Ошибки индекса (IndexError).
Попытка обратиться к несуществующему элементу списка.
В ML это аналогично обращению к несуществующей строке датасета.
"""

# Список моделей для ансамбля
models: list[str] = ["Random Forest", "SVM", "Logistic Regression"]

# Правильный доступ: индексы 0, 1, 2
print(f"Model 0: {models[0]}")
print(f"Model 1: {models[1]}")
print(f"Model 2: {models[2]}")

# Неправильный доступ: индекс 3 не существует!
# Это вызовет IndexError: list index out of range
# print(f"Model 3: {models[3]}")  # ЗАКОММЕНТИРОВАНО — раскомментируйте для теста

# Как избежать ошибки: проверить длину списка
print(f"\nДлина списка моделей: {len(models)}")
print(f"Последний допустимый индекс: {len(models) - 1}")

# Безопасный способ получить последний элемент
last_model: str = models[-1]  # Отрицательная индексация
print(f"\nПоследняя модель (через -1): {last_model}")

# Еще безопаснее: проверить индекс перед доступом
index: int = 5
if index < len(models):
    print(f"Model at index {index}: {models[index]}")
else:
    print(f"Ошибка: индекс {index} вне диапазона (0-{len(models)-1})")