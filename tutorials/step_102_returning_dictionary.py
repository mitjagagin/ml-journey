"""
Микро-шаг 102: Возврат словаря (Returning a Dictionary).
Функция возвращает словарь с несколькими именованными значениями.
В ML это используется для возврата нескольких метрик (числовых оценок
качества модели) из одной функции оценки.
"""

# Функция возвращает словарь с двумя метриками
def evaluate_model(correct: int, total: int) -> dict[str, float]:
    accuracy: float = correct / total
    error_rate: float = 1.0 - accuracy
    results: dict[str, float] = {
        "accuracy": accuracy,
        "error_rate": error_rate
    }
    return results

# Вызываем функцию и сохраняем результат в переменную
metrics: dict[str, float] = evaluate_model(85, 100)

# Обращаемся к отдельным значениям словаря по ключам
print("Результаты оценки модели:")
print(f"  Точность: {metrics['accuracy']}")
print(f"  Доля ошибок: {metrics['error_rate']}")