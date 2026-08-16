"""
Микро-шаг 69: Доступ к значениям словаря (Accessing Values in a Dictionary).
Извлечение значений по ключу и сохранение в переменные для вычислений.
В ML это используется для получения метрик из отчётов модели,
извлечения предсказаний из JSON-ответов API и чтения конфигураций.
"""

# Результаты оценки модели после обучения
evaluation_results: dict[str, float] = {
    'accuracy': 0.94,
    'precision': 0.91,
    'recall': 0.89,
    'f1_score': 0.90
}

# Извлекаем значения по ключам и сохраняем в переменные
accuracy_value: float = evaluation_results['accuracy']
f1_value: float = evaluation_results['f1_score']

print("Извлечённые метрики модели:")
print(f"  Accuracy: {accuracy_value}")
print(f"  F1 Score: {f1_value}")

# Используем извлечённые значения для принятия решения
threshold: float = 0.90

print("\nПроверка порога качества:")
if accuracy_value >= threshold:
    print(f"  Модель проходит по accuracy ({accuracy_value} >= {threshold})")
else:
    print(f"  Модель не проходит по accuracy ({accuracy_value} < {threshold})")

if f1_value >= threshold:
    print(f"  Модель проходит по F1 ({f1_value} >= {threshold})")
else:
    print(f"  Модель не проходит по F1 ({f1_value} < {threshold})")